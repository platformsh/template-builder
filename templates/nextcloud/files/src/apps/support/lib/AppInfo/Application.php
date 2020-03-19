<?php
declare(strict_types=1);
/**
 * @copyright Copyright (c) 2018, Morris Jobke <hey@morrisjobke.de>
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

namespace OCA\Support\AppInfo;

use OCA\Support\Notification\Notifier;
use OCA\Support\Subscription\SubscriptionAdapter;
use OCP\AppFramework\App;
use OCP\IUser;
use OCP\Support\Subscription\Exception\AlreadyRegisteredException;
use OCP\Support\Subscription\IRegistry;

class Application extends App {
	public function __construct() {
		parent::__construct('support', []);
	}

	public function register() {
		$container = $this->getContainer();
		$server = $container->getServer();

		/* @var $registry IRegistry */
		$registry = $container->query(IRegistry::class);
		$subscription = $container->query(SubscriptionAdapter::class);
		try {
			$registry->register($subscription);
		} catch (AlreadyRegisteredException $e) {
			$server->getLogger()->logException($e, ['message' => 'Multiple subscription adapters are registered.', 'app' => 'support']);
		}

		$user = $server->getUserSession()->getUser();
		if (!$user instanceof IUser) {
			// Nothing to do for guests
			return;
		}

		if ($server->getAppManager()->isEnabledForUser('notifications')) {
			// Notifications app is available, so we register.
			// Since notifications also work for non-admins we don't check this here.
			$this->registerNotifier();
		}
	}

	public function registerNotifier() {
		$notificationsManager = $this->getContainer()->getServer()->getNotificationManager();
		$notificationsManager->registerNotifier(function() {
			return  $this->getContainer()->query(Notifier::class);
		}, function() {
			$l = $this->getContainer()->getServer()->getL10N('support');
			return [
				'id' => 'support',
				'name' => $l->t('Subscription notifications'),
			];
		});
	}
}
