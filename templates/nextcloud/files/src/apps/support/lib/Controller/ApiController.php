<?php
/**
 * @copyright Copyright (c) 2018 Morris Jobke <hey@morrisjobke.de>
 *
 * @author Morris Jobke <hey@morrisjobke.de>
 *
 * @license GNU AGPL version 3 or any later version
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

namespace OCA\Support\Controller;

use OC\AppFramework\Http;
use OCA\Support\DetailManager;
use OCA\Support\Sections\ServerSection;
use OCA\Support\Service\SubscriptionService;
use OCP\AppFramework\Controller;
use OCP\AppFramework\Http\DataResponse;
use OCP\AppFramework\Http\RedirectResponse;
use OCP\Constants;
use OCP\Files\IRootFolder;
use OCP\Files\NotFoundException;
use OCP\IL10N;
use OCP\ILogger;
use OCP\IRequest;
use OCP\IURLGenerator;
use OCP\IUserSession;
use OCP\Security\ISecureRandom;
use OCP\Share\IManager;

class ApiController extends Controller {

	/** @var IURLGenerator */
	private $urlGenerator;
	/** @var SubscriptionService */
	private $subscriptionService;
	/** @var DetailManager */
	private $detailManager;
	/** @var ServerSection */
	private $serverSection;
	/** @var ILogger */
	private $logger;
	/** @var IL10N */
	private $l10n;
	/** @var IManager */
	private $shareManager;
	/** @var \OCP\Files\Folder */
	private $userFolder;
	/** @var ISecureRandom */
	private $random;
	/** @var string */
	private $userId;

	public function __construct($appName,
								IRequest $request,
								IURLGenerator $urlGenerator,
								SubscriptionService $subscriptionService,
								DetailManager $detailManager,
								ServerSection $serverSection,
								IRootFolder $rootFolder,
								IUserSession $userSession,
								ILogger $logger,
								IL10N $l10n,
								IManager $shareManager,
								ISecureRandom $random) {
		parent::__construct($appName, $request);

		$this->urlGenerator = $urlGenerator;
		$this->subscriptionService = $subscriptionService;
		$this->detailManager = $detailManager;
		$this->serverSection = $serverSection;
		$this->logger = $logger;
		$this->l10n = $l10n;
		$this->shareManager = $shareManager;
		$this->random = $random;
		$this->userId = $userSession->getUser()->getUID();

		// Register core details that are used in every report
		$this->detailManager->addSection($this->serverSection);

		$this->userFolder = $rootFolder->getUserFolder($this->userId);
	}

	public function setSubscriptionKey(string $subscriptionKey) {
		$this->subscriptionService->setSubscriptionKey(trim($subscriptionKey));

		return new RedirectResponse($this->urlGenerator->getAbsoluteURL($this->urlGenerator->linkToRoute('settings.AdminSettings.index', ['section' => 'support'])));
	}

	public function generateSystemReport() {
		try {
			$directory = $this->userFolder->get('System information');
		} catch (NotFoundException $e) {
			try {
				$directory = $this->userFolder->newFolder('System information');
			} catch (\Exception $ex) {
				$this->logger->logException($ex, ['app' => 'support', 'message' => 'Could not create folder "System information" to store generated report.', 'level' => ILogger::WARN]);
				$response = new DataResponse(['message' => $this->l10n->t('Could not create folder "System information" to store generated report.')]);
				$response->setStatus(Http::STATUS_INTERNAL_SERVER_ERROR);
				return $response;
			}
		}


		$date = (new \DateTime())->format('Y-m-d');
		$filename = $date . '.md';
		$filename = $directory->getNonExistingName($filename);

		try {
			$file = $directory->newFile($filename);
			$details = $this->detailManager->getRenderedDetails();
			$file->putContent($details);
		} catch (\Exception $e) {
			$this->logger->logException($e, ['app' => 'support', 'message' => 'Could not create file "' . $filename . '" to store generated report.', 'level' => ILogger::WARN]);
			$response = new DataResponse(['message' => $this->l10n->t('Could not create file "%s" to store generated report.', [ $filename ])]);
			$response->setStatus(Http::STATUS_INTERNAL_SERVER_ERROR);
			return $response;
		}

		try {
			$password = $this->random->generate(20);
			$share = $this->shareManager->newShare();
			$share->setNode($file);
			$share->setPermissions(Constants::PERMISSION_READ);
			$share->setShareType(\OC\Share\Constants::SHARE_TYPE_LINK);
			$share->setSharedBy($this->userId);
			$share->setPassword($password);

			if ($this->shareManager->shareApiLinkDefaultExpireDateEnforced()) {
				$expiry = new \DateTime();
				$expiry->add(new \DateInterval('P' . $this->shareManager->shareApiLinkDefaultExpireDays() . 'D'));
			} else {
				$expiry = new \DateTime();
				$expiry->add(new \DateInterval('P2W'));
			}

			$share->setExpirationDate($expiry);

			$share = $this->shareManager->createShare($share);
		} catch (\Exception $e) {
			$this->logger->logException($e, ['app' => 'support', 'message' => 'Could not share file "' . $filename . '".', 'level' => ILogger::WARN]);
			$response = new DataResponse(['message' => $this->l10n->t('Could not share file "%s".', [$filename])]);
			$response->setStatus(Http::STATUS_INTERNAL_SERVER_ERROR);
			return $response;
		}

		return new DataResponse(
			[
				'link' => $this->urlGenerator->linkToRouteAbsolute('files_sharing.sharecontroller.showShare', ['token' => $share->getToken()]),
				'password' => $password,
			],
			Http::STATUS_CREATED
		);
	}
}
