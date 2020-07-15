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

class statssearch extends ModuleGraph
{
    private $html = '';
    private $query = '';
    private $query_group_by = '';

    public function __construct()
    {
        $this->name = 'statssearch';
        $this->tab = 'analytics_stats';
        $this->version = '2.0.1';
        $this->author = 'PrestaShop';
        $this->need_instance = 0;

        parent::__construct();

        $this->query = 'SELECT `keywords`, COUNT(TRIM(`keywords`)) as occurences, MAX(results) as total
				FROM `'._DB_PREFIX_.'statssearch`
				WHERE 1
					'.Shop::addSqlRestriction().'
					AND `date_add` BETWEEN ';

        $this->query_group_by = 'GROUP BY `keywords`
				HAVING occurences > 1
				ORDER BY occurences DESC';

        $this->displayName = $this->trans('Shop search', array(), 'Modules.Statssearch.Admin');
        $this->description = $this->trans('Adds a tab to the Stats dashboard, showing which keywords have been searched by your store\'s visitors.', array(), 'Modules.Statssearch.Admin');
        $this->ps_versions_compliancy = array('min' => '1.7.1.0', 'max' => _PS_VERSION_);
    }

    public function install()
    {
        if (!parent::install() || !$this->registerHook('actionSearch') || !$this->registerHook('AdminStatsModules')) {
            return false;
        }

        return Db::getInstance()->execute('
		CREATE TABLE `'._DB_PREFIX_.'statssearch` (
			id_statssearch INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
			id_shop INTEGER UNSIGNED NOT NULL DEFAULT \'1\',
		  	id_shop_group INTEGER UNSIGNED NOT NULL DEFAULT \'1\',
			keywords VARCHAR(255) NOT NULL,
			results INT(6) NOT NULL DEFAULT 0,
			date_add DATETIME NOT NULL,
			PRIMARY KEY(id_statssearch)
		) ENGINE='._MYSQL_ENGINE_.' DEFAULT CHARSET=utf8');
    }

    public function uninstall()
    {
        if (!parent::uninstall()) {
            return false;
        }

        return (Db::getInstance()->execute('DROP TABLE `'._DB_PREFIX_.'statssearch`'));
    }

    /**
     * Insert keywords in statssearch table when a search is launched on FO
     */
    public function hookActionSearch($params)
    {
        $sql = 'INSERT INTO `'._DB_PREFIX_.'statssearch` (`id_shop`, `id_shop_group`, `keywords`, `results`, `date_add`)
				VALUES ('.(int)$this->context->shop->id.', '.(int)$this->context->shop->id_shop_group.', \''.pSQL($params['expr']).'\', '.(int)$params['total'].', NOW())';
        Db::getInstance()->execute($sql);
    }

    public function hookAdminStatsModules()
    {
        if (Tools::getValue('export')) {
            $this->csvExport(array('type' => 'pie'));
        }

        $result = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($this->query.ModuleGraph::getDateBetween().$this->query_group_by);
        $this->html = '
		<div class="panel-heading">
			'.$this->displayName.'
		</div>';
        $table = '
		<table class="table">
			<thead>
				<tr>
					<th><span class="title_box active">'.$this->trans('Keywords', array(), 'Modules.Statssearch.Admin').'</span></th>
					<th><span class="title_box active">'.$this->trans('Occurrences', array(), 'Modules.Statssearch.Admin').'</span></th>
					<th><span class="title_box active">'.$this->trans('Results', array(), 'Modules.Statssearch.Admin').'</span></th>
				</tr>
			</thead>
			<tbody>';

        foreach ($result as $row) {
            if (Tools::strlen($row['keywords']) >= Configuration::get('PS_SEARCH_MINWORDLEN')) {
                $table .= '<tr>
					<td>'.$row['keywords'].'</td>
					<td>'.$row['occurences'].'</td>
					<td>'.$row['total'].'</td>
				</tr>';
            }
        }
        $table .= '
			</tbody>
		</table>';

        if (count($result)) {
            $this->html .= '<div>'.$this->engine(array('type' => 'pie')).'</div>
							<a class="btn btn-default" href="'.Tools::safeOutput($_SERVER['REQUEST_URI']).'&export=1">
								<i class="icon-cloud-upload"></i> '.$this->trans('CSV Export', array(), 'Modules.Statssearch.Admin').'
							</a>'.$table;
        } else {
            $this->html .= '<p>'.$this->trans('Cannot find any keywords that have been searched for more than once.', array(), 'Modules.Statssearch.Admin').'</p>';
        }

        return $this->html;
    }

    protected function getData($layers)
    {
        $this->_titles['main'] = $this->trans('Top 10 keywords', array(), 'Modules.Statssearch.Admin');
        $total_result = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($this->query.$this->getDate().$this->query_group_by);
        $total = 0;
        $total2 = 0;
        foreach ($total_result as $total_row) {
            $total += $total_row['occurences'];
        }
        $result = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($this->query.$this->getDate().$this->query_group_by.' LIMIT 9');
        foreach ($result as $row) {
            if (!$row['occurences']) {
                continue;
            }
            $this->_legend[] = $row['keywords'];
            $this->_values[] = $row['occurences'];
            $total2 += $row['occurences'];
        }
        if ($total > $total2) {
            $this->_legend[] = $this->trans('Others', array(), 'Modules.Statssearch.Admin');
            $this->_values[] = $total - $total2;
        }
    }
}
