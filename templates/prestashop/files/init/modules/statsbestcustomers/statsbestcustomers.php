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

class statsbestcustomers extends ModuleGrid
{
    private $html;
    private $query;
    private $columns;
    private $default_sort_column;
    private $default_sort_direction;
    private $empty_message;
    private $paging_message;

    public function __construct()
    {
        $this->name = 'statsbestcustomers';
        $this->tab = 'analytics_stats';
        $this->version = '2.0.2';
        $this->author = 'PrestaShop';
        $this->need_instance = 0;

        parent::__construct();

        $this->default_sort_column = 'totalMoneySpent';
        $this->default_sort_direction = 'DESC';
        $this->empty_message = $this->trans('Empty recordset returned', array(), 'Modules.Statsbestcustomers.Admin');
        $this->paging_message = $this->trans('Displaying %1$s of %2$s', array('{0} - {1}', '{2}'), 'Admin.Global');

        $currency = new Currency(Configuration::get('PS_CURRENCY_DEFAULT'));

        $this->columns = array(
            array(
                'id' => 'lastname',
                'header' => $this->trans('Last Name', array(), 'Admin.Global'),
                'dataIndex' => 'lastname',
                'align' => 'center'
            ),
            array(
                'id' => 'firstname',
                'header' => $this->trans('First Name', array(), 'Admin.Global'),
                'dataIndex' => 'firstname',
                'align' => 'center'
            ),
            array(
                'id' => 'email',
                'header' => $this->trans('Email', array(), 'Admin.Global'),
                'dataIndex' => 'email',
                'align' => 'center'
            ),
            array(
                'id' => 'totalVisits',
                'header' => $this->trans('Visits', array(), 'Admin.Shopparameters.Feature'),
                'dataIndex' => 'totalVisits',
                'align' => 'center'
            ),
            array(
                'id' => 'totalValidOrders',
                'header' => $this->trans('Valid orders', array(), 'Modules.Statsbestcustomers.Admin'),
                'dataIndex' => 'totalValidOrders',
                'align' => 'center'
            ),
            array(
                'id' => 'totalMoneySpent',
                'header' => $this->trans('Money spent', array(), 'Modules.Statsbestcustomers.Admin').' ('.Tools::safeOutput($currency->iso_code).')',
                'dataIndex' => 'totalMoneySpent',
                'align' => 'center'
            )
        );

        $this->displayName = $this->trans('Best customers', array(), 'Modules.Statsbestcustomers.Admin');
        $this->description = $this->trans('Adds a list of the best customers to the Stats dashboard.', array(), 'Modules.Statsbestcustomers.Admin');
        $this->ps_versions_compliancy = array('min' => '1.7.1.0', 'max' => _PS_VERSION_);
    }

    public function install()
    {
        return (parent::install() && $this->registerHook('AdminStatsModules'));
    }

    public function hookAdminStatsModules($params)
    {
        $engine_params = array(
            'id' => 'id_customer',
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
		<div class="panel-heading">
			'.$this->displayName.'
		</div>
		<h4>'.$this->trans('Guide', array(), 'Admin.Global').'</h4>
			<div class="alert alert-warning">
				<h4>'.$this->trans('Develop clients\' loyalty', array(), 'Modules.Statsbestcustomers.Admin').'</h4>
				<div>
					'.$this->trans('Keeping a client can be more profitable than gaining a new one. That is one of the many reasons it is necessary to cultivate customer loyalty.', array(), 'Modules.Statsbestcustomers.Admin').' <br />
					'.$this->trans('Word of mouth is also a means for getting new, satisfied clients. A dissatisfied customer can hurt your e-reputation and obstruct future sales goals.', array(), 'Modules.Statsbestcustomers.Admin').'<br />
					'.$this->trans('In order to achieve this goal, you can organize:', array(), 'Modules.Statsbestcustomers.Admin').'
					<ul>
						<li>'.$this->trans('Punctual operations: commercial rewards (personalized special offers, product or service offered), non commercial rewards (priority handling of an order or a product), pecuniary rewards (bonds, discount coupons, payback).', array(), 'Modules.Statsbestcustomers.Admin').'</li>
						<li>'.$this->trans('Sustainable operations: loyalty points or cards, which not only justify communication between merchant and client, but also offer advantages to clients (private offers, discounts).', array(), 'Modules.Statsbestcustomers.Admin').'</li>
					</ul>
					'.$this->trans('These operations encourage clients to buy products and visit your online store more regularly.', array(), 'Modules.Statsbestcustomers.Admin').'
				</div>
			</div>
		'.$this->engine($engine_params).'
		<a class="btn btn-default export-csv" href="'.Tools::safeOutput($_SERVER['REQUEST_URI'].'&export=').'1">
			<i class="icon-cloud-upload"></i> '.$this->trans('CSV Export', array(), 'Admin.Global').'
		</a>';

        return $this->html;
    }

    public function getData()
    {
        $this->query = '
		SELECT SQL_CALC_FOUND_ROWS c.`id_customer`, c.`lastname`, c.`firstname`, c.`email`,
			COUNT(co.`id_connections`) as totalVisits,
			IFNULL((
				SELECT ROUND(SUM(IFNULL(op.`amount`, 0) / cu.conversion_rate), 2)
				FROM `'._DB_PREFIX_.'orders` o
				LEFT JOIN `'._DB_PREFIX_.'order_payment` op ON o.reference = op.order_reference
				LEFT JOIN `'._DB_PREFIX_.'currency` cu ON o.id_currency = cu.id_currency
				WHERE o.id_customer = c.id_customer
				AND o.invoice_date BETWEEN '.$this->getDate().'
				AND o.valid
			), 0) as totalMoneySpent,
			IFNULL((
				SELECT COUNT(*)
				FROM `'._DB_PREFIX_.'orders` o
				WHERE o.id_customer = c.id_customer
				AND o.invoice_date BETWEEN '.$this->getDate().'
				AND o.valid
			), 0) as totalValidOrders
		FROM `'._DB_PREFIX_.'customer` c
		LEFT JOIN `'._DB_PREFIX_.'guest` g ON c.`id_customer` = g.`id_customer`
		LEFT JOIN `'._DB_PREFIX_.'connections` co ON g.`id_guest` = co.`id_guest`
		WHERE co.date_add BETWEEN '.$this->getDate()
            .Shop::addSqlRestriction(Shop::SHARE_CUSTOMER, 'c').
            ' GROUP BY c.`id_customer`, c.`lastname`, c.`firstname`, c.`email`';

        if (Validate::IsName($this->_sort)) {
            $this->query .= ' ORDER BY `'.bqSQL($this->_sort).'`';
            if (isset($this->_direction) && Validate::isSortDirection($this->_direction)) {
                $this->query .= ' '.$this->_direction;
            }
        }

        if (($this->_start === 0 || Validate::IsUnsignedInt($this->_start)) && Validate::IsUnsignedInt($this->_limit)) {
            $this->query .= ' LIMIT '.(int)$this->_start.', '.(int)$this->_limit;
        }

        $this->_values = Db::getInstance(_PS_USE_SQL_SLAVE_)->executeS($this->query);
        $this->_totalCount = Db::getInstance(_PS_USE_SQL_SLAVE_)->getValue('SELECT FOUND_ROWS()');
    }
}
