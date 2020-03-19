<?php
/**
 * @author Joas Schilling <coding@schilljs.com>
 *
 * @copyright Copyright (c) 2016, ownCloud, Inc.
 * @license AGPL-3.0
 *
 * This code is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License, version 3,
 * as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License, version 3,
 * along with this program.  If not, see <http://www.gnu.org/licenses/>
 *
 */

namespace OCA\Survey_Client\BackgroundJobs;

use OC\BackgroundJob\QueuedJob;

class AdminNotification extends QueuedJob {
	protected function run($argument) {
		$manager = \OC::$server->getNotificationManager();
		$urlGenerator = \OC::$server->getURLGenerator();

		$notification = $manager->createNotification();

		$notification->setApp('survey_client')
			->setDateTime(new \DateTime())
			->setSubject('updated')
			->setObject('dummy', 23);

		$enableAction = $notification->createAction();
		$enableAction->setLabel('enable')
			->setLink($urlGenerator->getAbsoluteURL('ocs/v2.php/apps/survey_client/api/v1/monthly'), 'POST')
			->setPrimary(true);
		$notification->addAction($enableAction);

		$disableAction = $notification->createAction();
		$disableAction->setLabel('disable')
			->setLink($urlGenerator->getAbsoluteURL('ocs/v2.php/apps/survey_client/api/v1/monthly'), 'DELETE')
			->setPrimary(false);
		$notification->addAction($disableAction);

		$adminGroup = \OC::$server->getGroupManager()->get('admin');
		foreach ($adminGroup->getUsers() as $admin) {
			$notification->setUser($admin->getUID());
			$manager->notify($notification);
		}

	}
}
