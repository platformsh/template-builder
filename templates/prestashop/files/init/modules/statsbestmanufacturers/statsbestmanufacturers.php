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

class statsbestmanufacturers extends ModuleGrid
{
    private $html = null;
    private $query = null;
    private $columns = null;
    private $default_sort_column = null;
    private $default_sort_direction = null;
    private $empty_message = null;
    private $paging_message = null;

    public function __construct()
    {
        $this->name = 'statsbestmanufacturers';
        $this->tab = 'analytics_stats';
        $this->version = '2.0.0';
        $this->author = 'PrestaShop';
        $this->need_instance = 0;

        parent::__construct();

        $this->default_sort_column = 'sales';
        $this->default_sort_direction = 'DESC';
        $this->empty_message = $this->trans('Empty recordset returned.', array(), 'Admin.Notifications.Info');
        $this->paging_message = $this->trans('Displaying %1$s of %2$s', array('{0} - {1}', '{2}'), 'Admin.Global');

        $this->columns = array(
            array(
                'id' => 'name',
                'header' => $this->trans('Name', array(), 'Admin.Global'),
                'dataIndex' => 'name',
                'align' => 'left',
                'width' => 200
            ),
            array(
                'id' => 'quantity',
                'header' => $this->trans('Quantity sold', array(), 'Admin.Global'),
                'dataIndex' => 'quantity',
                'width' => 60,
                'align' => 'right'
            ),
            array(
                'id' => 'sales',
                'header' => $this->trans('Total paid', array(), 'Modules.Statsbestmanufacturers.Admin'),
                'dataIndex' => 'sales',
                'width' => 60,
                'align' => 'right'
            )
        );

        $this->displayName = $this->trans('Best brands', array(), 'Modules.Statsbestmanufacturers.Admin');
        $this->description = $this->trans('Adds a list of the best brands to the Stats dashboard.', array(), 'Modules.Statsbestmanufacturers.Admin');
        $this->ps_versions_compliancy = array('min' => '1.7.1.0', 'max' => _PS_VERSION_);
    }

    public function install()
    {
        return (parent::install() && $this->registerHook('AdminStatsModules'));
    }

    public function hookAdminStatsModules($params)
    {
        $engine_params = array(
            'id' => 'id_category',
            'title' => $this->displayName,
            'columns' => $this->columns,
            'defaultSortColumn' => $this->default_sort_column,
            'defaultSortDirection' => $this->default_sort_direction,
            'emptyMessage' => $this->empty_message,
            'pagingMessage' => $this->paging_message
        );

        if (Tools::getValue('export')) {
            $this->csvExport($engine_params);
        }

        $this->html = '
		<fieldset>
			<legend><img alt="'.$this->name.'" src="../modules/'.$this->name.'/logo.gif" /> '.$this->displayName.'</legend>
			'.$this->engine($engine_params).'<br />
			<a href="'.Tools::safeOutput($_SERVER['REQUEST_URI'].'&export=1').'"><img alt="asterisk" src="../img/admin/asterisk.gif" />'.$this->trans('CSV Export', array(), 'Admin.Global').'</a>
		</fieldset>
		';

        return $this->html;
    }

    public function getTotalCount()
    {
        $sql = 'SELECT COUNT(DISTINCT(m.id_manufacturer))
				FROM '._DB_PREFIX_.'order_detail od
				LEFT JOIN '._DB_PREFIX_.'product p ON (p.id_product = od.product_id)
				LEFT JOIN '._DB_PREFIX_.'orders o ON (o.id_order = od.id_order)
				LEFT JOIN '._DB_PREFIX_.'manufacturer m ON (m.id_manufacturer = p.id_manufacturer)
				WHERE o.invoice_date BETWEEN '.$this->getDate()
            .Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o').
            'AND o.valid = 1
			AND m.id_manufacturer IS NOT NULL';

        return Db::getInstance()->getValue($sql);
    }

    public function getData()
    {
        $this->_totalCount = $this->getTotalCount();

        $this->query = 'SELECT m.name, SUM(od.product_quantity) as quantity, ROUND(SUM(od.product_quantity * od.product_price) / c.conversion_rate, 2) as sales
				FROM '._DB_PREFIX_.'order_detail od
				LEFT JOIN '._DB_PREFIX_.'product p ON (p.id_product = od.product_id)
				LEFT JOIN '._DB_PREFIX_.'orders o ON (o.id_order = od.id_order)
				LEFT JOIN '._DB_PREFIX_.'currency c ON (c.id_currency = o.id_currency)
				LEFT JOIN '._DB_PREFIX_.'manufacturer m ON (m.id_manufacturer = p.id_manufacturer)
				WHERE o.invoice_date BETWEEN '.$this->getDate().'
					'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o').'
					AND o.valid = 1
					AND m.id_manufacturer IS NOT NULL
				GROUP BY p.id_manufacturer';

        if (Validate::IsName($this->_sort)) {
            $this->query .= ' ORDER BY `'.bqSQL($this->_sort).'`';
            if (isset($this->_direction) && Validate::isSortDirection($this->_direction)) {
                $this->query .= ' '.$this->_direction;
            }
        }

        if (($this->_start === 0 || Validate::IsUnsignedInt($this->_start)) && Validate::IsUnsignedInt($this->_limit)) {
            $this->query .= ' LIMIT '.(int)$this->_start.', '.(int)$this->_limit;
        }

        $this->_values = Db::getInstance()->executeS($this->query);
    }
}
