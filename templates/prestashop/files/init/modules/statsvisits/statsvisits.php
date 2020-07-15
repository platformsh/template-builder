<?php
/*
* 2007-2015 PrestaShop
*
* NOTICE OF LICENSE
*
* This source file is subject to the Academic Free License (AFL 3.0)
* that is bundled with this package in the file LICENSE.txt.
* It is also available through the world-wide-web at this URL:
* http://opensource.org/licenses/afl-3.0.php
* If you did not receive a copy of the license and are unable to
* obtain it through the world-wide-web, please send an email
* to license@prestashop.com so we can send you a copy immediately.
*
* DISCLAIMER
*
* Do not edit or add to this file if you wish to upgrade PrestaShop to newer
* versions in the future. If you wish to customize PrestaShop for your
* needs please refer to http://www.prestashop.com for more information.
*
*  @author PrestaShop SA <contact@prestashop.com>
*  @copyright  2007-2015 PrestaShop SA
*  @license    http://opensource.org/licenses/afl-3.0.php  Academic Free License (AFL 3.0)
*  International Registered Trademark & Property of PrestaShop SA
*/

if (!defined('_PS_VERSION_')) {
    exit;
}

class statsvisits extends ModuleGraph
{
    private $html = '';
    private $query = '';

    public function __construct()
    {
        $this->name = 'statsvisits';
        $this->tab = 'analytics_stats';
        $this->version = '2.0.2';
        $this->author = 'PrestaShop';
        $this->need_instance = 0;

        parent::__construct();

        $this->displayName = $this->trans('Visits and Visitors', array(), 'Modules.Statsvisits.Admin');
        $this->description = $this->trans('Adds statistics about your visits and visitors to the Stats dashboard.', array(), 'Modules.Statsvisits.Admin');
        $this->ps_versions_compliancy = array('min' => '1.7.1.0', 'max' => _PS_VERSION_);
    }

    public function install()
    {
        return parent::install() && $this->registerHook('AdminStatsModules');
    }

    public function getTotalVisits()
    {
        $sql = 'SELECT COUNT(c.`id_connections`)
				FROM `'._DB_PREFIX_.'connections` c
				WHERE c.`date_add` BETWEEN '.ModuleGraph::getDateBetween().'
					'.Shop::addSqlRestriction(false, 'c');

        return Db::getInstance(_PS_USE_SQL_SLAVE_)->getValue($sql);
    }

    public function getTotalGuests()
    {
        $sql = 'SELECT COUNT(DISTINCT c.`id_guest`)
				FROM `'._DB_PREFIX_.'connections` c
				WHERE c.`date_add` BETWEEN '.ModuleGraph::getDateBetween().'
					'.Shop::addSqlRestriction(false, 'c');

        return Db::getInstance(_PS_USE_SQL_SLAVE_)->getValue($sql);
    }

    public function hookAdminStatsModules()
    {
        $graph_params = array(
            'layers' => 2,
            'type' => 'line',
            'option' => 3,
        );

        $total_visits = $this->getTotalVisits();
        $total_guests = $this->getTotalGuests();
        if (Tools::getValue('export')) {
            $this->csvExport(array(
                'layers' => 2,
                'type' => 'line',
                'option' => 3
            ));
        }
        $this->html = '
		<div class="panel-heading">
			'.$this->displayName.'
		</div>
		<h4>'.$this->trans('Guide', array(), 'Admin.Global').'</h4>
			<div class="alert alert-warning">
				<h4>'.$this->trans('Determine the interest of a visit', array(), 'Modules.Statsvisits.Admin').'</h4>
				<p>
					'.$this->trans('The visitors\' evolution graph strongly resembles the visits\' graph, but provides additional information:', array(), 'Modules.Statsvisits.Admin').'<br />
				</p>
				<ul>
					<li>'.$this->trans('If this is the case, congratulations, your website is well planned and pleasing. Glad to see that you\'ve been paying attention.', array(), 'Modules.Statsvisits.Admin').'</li>
					<li>'.$this->trans('Otherwise, the conclusion is not so simple. The problem can be aesthetic or ergonomic. It is also possible that many visitors have mistakenly visited your URL without possessing a particular interest in your shop. This strange and ever-confusing phenomenon is most likely cause by search engines. If this is the case, you should consider revising your SEO structure.', array(), 'Modules.Statsvisits.Admin').'</li>
				</ul>
				<p>
					'.$this->trans('This information is mostly qualitative. It is up to you to determine the interest of a disjointed visit.', array(), 'Modules.Statsvisits.Admin').'
				</p>
			</div>
			<div class="alert alert-info">
				'.$this->trans('A visit corresponds to an internet user coming to your shop, and until the end of their session, only one visit is counted.', array(), 'Modules.Statsvisits.Admin').'
				'.$this->trans('A visitor is an unknown person who has not registered or logged into your store. A visitor can also be considered a person who has visited your shop multiple times.', array(), 'Modules.Statsvisits.Admin').'
			</div>
			<div class="row row-margin-bottom">
				<div class="col-lg-12">
					<div class="col-lg-8">
						'.($total_visits ? $this->engine($graph_params).'
					</div>
					<div class="col-lg-4">
						<ul class="list-unstyled">
							<li>'.$this->trans('Total visits:', array(), 'Modules.Statsvisits.Admin').' <span class="totalStats">'.$total_visits.'</span></li>
							<li>'.$this->trans('Total visitors:', array(), 'Modules.Statsvisits.Admin').' <span class="totalStats">'.$total_guests.'</span></li>
						</ul>
						<hr/>
						<a class="btn btn-default export-csv" href="'.Tools::safeOutput($_SERVER['REQUEST_URI'].'&export=1').'">
							<i class="icon-cloud-upload"></i> '.$this->trans('CSV Export', array(), 'Modules.Statsvisits.Admin').'
						</a> ' : '').'
					</div>
				</div>
			</div>';

        return $this->html;
    }

    public function setOption($option, $layers = 1)
    {
        switch ($option) {
            case 3:
                $this->_titles['main'][0] = $this->trans('Number of visits and unique visitors', array(), 'Modules.Statsvisits.Admin');
                $this->_titles['main'][1] = $this->trans('Visits', array(), 'Admin.Shopparameters.Feature');
                $this->_titles['main'][2] = $this->trans('Visitors', array(), 'Admin.Shopparameters.Feature');
                $this->query[0] = 'SELECT date_add, COUNT(`date_add`) as total
					FROM `'._DB_PREFIX_.'connections`
					WHERE 1
						'.Shop::addSqlRestriction().'
						AND `date_add` BETWEEN ';
                $this->query[1] = 'SELECT date_add, COUNT(DISTINCT `id_guest`) as total
					FROM `'._DB_PREFIX_.'connections`
					WHERE 1
						'.Shop::addSqlRestriction().'
						AND `date_add` BETWEEN ';
                break;
        }
    }

    protected function getData($layers)
    {
        $this->setDateGraph($layers, true);
    }

    protected function setAllTimeValues($layers)
    {
        for ($i = 0; $i < $layers; $i++) {
            $result = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($this->query[$i].$this->getDate().' GROUP BY LEFT(date_add, 4)');
            foreach ($result as $row) {
                $this->_values[$i][(int)Tools::substr($row['date_add'], 0, 4)] = (int)$row['total'];
            }
        }
    }

    protected function setYearValues($layers)
    {
        for ($i = 0; $i < $layers; $i++) {
            $result = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($this->query[$i].$this->getDate().' GROUP BY LEFT(date_add, 7)');
            foreach ($result as $row) {
                $this->_values[$i][(int)Tools::substr($row['date_add'], 5, 2)] = (int)$row['total'];
            }
        }
    }

    protected function setMonthValues($layers)
    {
        for ($i = 0; $i < $layers; $i++) {
            $result = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($this->query[$i].$this->getDate().' GROUP BY LEFT(date_add, 10)');
            foreach ($result as $row) {
                $this->_values[$i][(int)Tools::substr($row['date_add'], 8, 2)] = (int)$row['total'];
            }
        }
    }

    protected function setDayValues($layers)
    {
        for ($i = 0; $i < $layers; $i++) {
            $result = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($this->query[$i].$this->getDate().' GROUP BY LEFT(date_add, 13)');
            foreach ($result as $row) {
                $this->_values[$i][(int)Tools::substr($row['date_add'], 11, 2)] = (int)$row['total'];
            }
        }
    }
}
