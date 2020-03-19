<?php
declare(strict_types=1);

/**
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

namespace OCA\Support\Subscription;

use OCA\Support\Service\SubscriptionService;
use OCP\Support\Subscription\ISubscription;
use OCP\Support\Subscription\ISupportedApps;

class SubscriptionAdapter implements ISubscription, ISupportedApps {

	/** @var SubscriptionService */
	private $subscriptionService;

	public function __construct(SubscriptionService $subscriptionService) {
		$this->subscriptionService = $subscriptionService;
	}

	/**
	 * Indicates if a valid subscription is available
	 *
	 * @return bool
	 */
	public function hasValidSubscription(): bool {
		list(
			$instanceSize,
			$hasSubscription,
			$isInvalidSubscription,
			$isOverLimit,
			$subscriptionInfo
			) = $this->subscriptionService->getSubscriptionInfo();

		return !$isInvalidSubscription;
	}

	private function subscriptionNotExpired(string $endDate): bool {
		$subscriptionEndDate = new \DateTime($endDate);
		$now = new \DateTime();
		if ($now >= $subscriptionEndDate) {
			return false;
		}
		return true;
	}

	/**
	 * Fetches the list of app IDs that are supported by the subscription
	 *
	 * @since 17.0.0
	 */
	public function getSupportedApps(): array {
		list(
			$instanceSize,
			$hasSubscription,
			$isInvalidSubscription,
			$isOverLimit,
			$subscriptionInfo
			) = $this->subscriptionService->getSubscriptionInfo();
		$hasValidGroupwareSubscription = $this->subscriptionNotExpired($subscriptionInfo['groupware']['endDate'] ?? 'now');
		$hasValidTalkSubscription = $this->subscriptionNotExpired($subscriptionInfo['talk']['endDate'] ?? 'now');
		$hasValidCollaboraSubscription = $this->subscriptionNotExpired($subscriptionInfo['collabora']['endDate'] ?? 'now');
		$hasValidOnlyOfficeSubscription = $this->subscriptionNotExpired($subscriptionInfo['onlyoffice']['endDate'] ?? 'now');

		$filesSubscription = [
			'accessibility',
			'activity',
			'admin_audit',
			'circles',
			'comments',
			'data_request',
			'dav',
			'encryption',
			'external',
			'federatedfilesharing',
			'federation',
			'files',
			'files_accesscontrol',
			'files_antivirus',
			'files_automatedtagging',
			'files_external',
			'files_fulltextsearch',
			'files_fulltextsearch_tesseract',
			'files_pdfviewer',
			'files_retention',
			'files_sharing',
			'files_trashbin',
			'files_versions',
			'files_videoplayer',
			'firstrunwizard',
			'fulltextsearch',
			'fulltextsearch_elasticsearch',
			'gallery',
			'logreader',
			'lookup_server_connector',
			'nextcloud_announcements',
			'notifications',
			'password_policy',
			'provisioning_api',
			'serverinfo',
			'sharebymail',
			'sharepoint',
			'socialsharing_diaspora',
			'socialsharing_email',
			'socialsharing_facebook',
			'socialsharing_twitter',
			'support',
			'systemtags',
			'text',
			'theming',
			'updatenotification',
			'user_ldap',
			'user_saml',
			'viewer',
			'workflowengine',
		];

		$nextcloudVersion = \OCP\Util::getVersion()[0];

		if ($nextcloudVersion >= 16) {
			$filesSubscription[] = 'files_rightclick';
			$filesSubscription[] = 'groupfolders';
			$filesSubscription[] = 'guests';
			$filesSubscription[] = 'privacy';
			$filesSubscription[] = 'recommendations';
			$filesSubscription[] = 'terms_of_service';
			$filesSubscription[] = 'text';
		}
		if ($nextcloudVersion >= 17) {
			$filesSubscription[] = 'twofactor_totp';
			$filesSubscription[] = 'twofactor_u2f';
		}
		if ($nextcloudVersion  < 17) {
			$filesSubscription[] = 'files_texteditor';
		}

		$supportedApps = [];

		if ($hasSubscription) {
			$supportedApps = array_merge($supportedApps, $filesSubscription);
		}
		if ($hasValidGroupwareSubscription) {
			$supportedApps[] = 'calendar';
			$supportedApps[] = 'contacts';
			$supportedApps[] = 'deck';
			$supportedApps[] = 'mail';
		}
		if ($hasValidTalkSubscription) {
			$supportedApps[] = 'talk';
		}
		if ($hasValidCollaboraSubscription) {
			$supportedApps[] = 'richdocuments';
		}
		if ($hasValidOnlyOfficeSubscription) {
			$supportedApps[] = 'onlyoffice';
		}

		if (isset($subscriptionInfo['supportedApps'])) {
			foreach ($subscriptionInfo['supportedApps'] as $app) {
				if ($app !== '' && !in_array($app, $supportedApps)) {
					$supportedApps[] = $app;
				}
			}
		}

		return $supportedApps;
	}

	/**
	 * Indicates if the subscription has extended support
	 *
	 * @since 17.0.0
	 */
	public function hasExtendedSupport(): bool {
		$subscriptionInfo = $this->subscriptionService->getMinimalSubscriptionInfo();
		return $subscriptionInfo['extendedSupport'] ?? false;
	}
}
