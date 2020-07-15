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

class statsforecast extends Module
{
    private $html = '';
    private $t1 = 0;
    private $t2 = 0;
    private $t3 = 0;
    private $t4 = 0;
    private $t5 = 0;
    private $t6 = 0;
    private $t7 = 0;
    private $t8 = 0;

    public function __construct()
    {
        $this->name = 'statsforecast';
        $this->tab = 'analytics_stats';
        $this->version = '2.0.3';
        $this->author = 'PrestaShop';
        $this->need_instance = 0;

        parent::__construct();

        $this->displayName = $this->trans('Stats Dashboard', array(), 'Modules.Statsforecast.Admin');
        $this->description = $this->trans('This is the main module for the Stats dashboard. It displays a summary of all your current statistics.', array(), 'Modules.Statsforecast.Admin');
        $this->ps_versions_compliancy = array('min' => '1.7.1.0', 'max' => _PS_VERSION_);
    }

    public function install()
    {
        return (parent::install() && $this->registerHook('AdminStatsModules'));
    }

    public function getContent()
    {
        Tools::redirectAdmin('index.php?controller=AdminStats&module=statsforecast&token='.Tools::getAdminTokenLite('AdminStats'));
    }

    public function hookAdminStatsModules()
    {
        $ru = AdminController::$currentIndex.'&module='.$this->name.'&token='.Tools::getValue('token');

        $db = Db::getInstance();

        if (!isset($this->context->cookie->stats_granularity)) {
            $this->context->cookie->stats_granularity = 10;
        }
        if (Tools::isSubmit('submitIdZone')) {
            $this->context->cookie->stats_id_zone = (int)Tools::getValue('stats_id_zone');
        }
        if (Tools::isSubmit('submitGranularity')) {
            $this->context->cookie->stats_granularity = Tools::getValue('stats_granularity');
        }

        $currency = $this->context->currency;
        $employee = $this->context->employee;

        $from = max(strtotime(_PS_CREATION_DATE_.' 00:00:00'), strtotime($employee->stats_date_from.' 00:00:00'));
        $to = strtotime($employee->stats_date_to.' 23:59:59');
        $to2 = min(time(), $to);
        $interval = ($to - $from) / 60 / 60 / 24;
        $interval2 = ($to2 - $from) / 60 / 60 / 24;
        $prop30 = $interval / $interval2;

        if ($this->context->cookie->stats_granularity == 7) {
            $interval_avg = $interval2 / 30;
        }
        if ($this->context->cookie->stats_granularity == 4) {
            $interval_avg = $interval2 / 365;
        }
        if ($this->context->cookie->stats_granularity == 10) {
            $interval_avg = $interval2;
        }
        if ($this->context->cookie->stats_granularity == 42) {
            $interval_avg = $interval2 / 7;
        }

        $data_table = array();
        if ($this->context->cookie->stats_granularity == 10) {
            for ($i = $from; $i <= $to2; $i = strtotime('+1 day', $i)) {
                $data_table[date('Y-m-d', $i)] = array(
                    'fix_date' => date('Y-m-d', $i),
                    'countOrders' => 0,
                    'countProducts' => 0,
                    'totalSales' => 0
                );
            }
        }

        $date_from_gadd = ($this->context->cookie->stats_granularity != 42
            ? 'LEFT(date_add, '.(int)$this->context->cookie->stats_granularity.')'
            : 'IFNULL(MAKEDATE(YEAR(date_add),DAYOFYEAR(date_add)-WEEKDAY(date_add)), CONCAT(YEAR(date_add),"-01-01*"))');

        $date_from_ginvoice = ($this->context->cookie->stats_granularity != 42
            ? 'LEFT(invoice_date, '.(int)$this->context->cookie->stats_granularity.')'
            : 'IFNULL(MAKEDATE(YEAR(invoice_date),DAYOFYEAR(invoice_date)-WEEKDAY(invoice_date)), CONCAT(YEAR(invoice_date),"-01-01*"))');

        $result = $db->query('
		SELECT
			'.$date_from_ginvoice.' as fix_date,
			COUNT(*) as countOrders,
			SUM((SELECT SUM(od.product_quantity) FROM '._DB_PREFIX_.'order_detail od WHERE o.id_order = od.id_order)) as countProducts,
			SUM(o.total_paid_tax_excl / o.conversion_rate) as totalSales
		FROM '._DB_PREFIX_.'orders o
		WHERE o.valid = 1
		AND o.invoice_date BETWEEN '.ModuleGraph::getDateBetween().'
		'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o').'
		GROUP BY '.$date_from_ginvoice);
        while ($row = $db->nextRow($result)) {
            $data_table[$row['fix_date']] = $row;
        }

        $this->html .= '<div>
			<div class="panel-heading"><i class="icon-dashboard"></i> '.$this->displayName.'</div>
			<div class="alert alert-info">'.$this->trans('The listed amounts do not include tax.', array(), 'Modules.Statsforecast.Admin').'</div>
			<form id="granularity" action="'.Tools::safeOutput($ru).'#granularity" method="post" class="form-horizontal">
				<div class="row row-margin-bottom">
					<label class="control-label col-lg-3">
						'.$this->trans('Time frame', array(), 'Modules.Statsforecast.Admin').'
					</label>
					<div class="col-lg-2">
						<input type="hidden" name="submitGranularity" value="1" />
						<select name="stats_granularity" onchange="this.form.submit();">
							<option value="10">'.$this->trans('Daily', array(), 'Modules.Statsforecast.Admin').'</option>
							<option value="42" '.($this->context->cookie->stats_granularity == '42' ? 'selected="selected"' : '').'>'.$this->trans('Weekly', array(), 'Modules.Statsforecast.Admin').'</option>
							<option value="7" '.($this->context->cookie->stats_granularity == '7' ? 'selected="selected"' : '').'>'.$this->trans('Monthly', array(), 'Modules.Statsforecast.Admin').'</option>
							<option value="4" '.($this->context->cookie->stats_granularity == '4' ? 'selected="selected"' : '').'>'.$this->trans('Yearly', array(), 'Modules.Statsforecast.Admin').'</option>
						</select>
					</div>
				</div>
			</form>

			<table class="table">
				<thead>
					<tr>
						<th></th>
						<th class="text-center"><span class="title_box active">'.$this->trans('Visits', array(), 'Admin.Shopparameters.Feature').'</span></th>
						<th class="text-center"><span class="title_box active">'.$this->trans('Registrations', array(), 'Admin.Shopparameters.Feature').'</span></th>
						<th class="text-center"><span class="title_box active">'.$this->trans('Placed orders', array(), 'Modules.Statsforecast.Admin').'</span></th>
						<th class="text-center"><span class="title_box active">'.$this->trans('Bought items', array(), 'Modules.Statsforecast.Admin').'</span></th>
						<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of registrations', array(), 'Modules.Statsforecast.Admin').'</span></th>
						<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of orders', array(), 'Modules.Statsforecast.Admin').'</span></th>
						<th class="text-center"><span class="title_box active">'.$this->trans('Revenue', array(), 'Modules.Statsforecast.Admin').'</span></th>
					</tr>
				</thead>';

        $visit_array = array();
        $sql = 'SELECT '.$date_from_gadd.' as fix_date, COUNT(*) as visits
				FROM '._DB_PREFIX_.'connections c
				WHERE c.date_add BETWEEN '.ModuleGraph::getDateBetween().'
				'.Shop::addSqlRestriction(false, 'c').'
				GROUP BY '.$date_from_gadd;
        $visits = Db::getInstance()->query($sql);
        while ($row = $db->nextRow($visits)) {
            $visit_array[$row['fix_date']] = $row['visits'];
        }

        foreach ($data_table as $row) {
            $visits_today = (int)(isset($visit_array[$row['fix_date']]) ? $visit_array[$row['fix_date']] : 0);

            $date_from_greg = ($this->context->cookie->stats_granularity != 42
                ? 'LIKE \''.$row['fix_date'].'%\''
                : 'BETWEEN \''.Tools::substr($row['fix_date'], 0, 10).' 00:00:00\' AND DATE_ADD(\''.Tools::substr($row['fix_date'], 0, 8).Tools::substr($row['fix_date'], 8, 2).' 23:59:59\', INTERVAL 7 DAY)');
            $row['registrations'] = Db::getInstance()->getValue('
			SELECT COUNT(*) FROM '._DB_PREFIX_.'customer
			WHERE date_add BETWEEN '.ModuleGraph::getDateBetween().'
			AND date_add '.$date_from_greg
                .Shop::addSqlRestriction(Shop::SHARE_CUSTOMER));

            $this->html .= '
			<tr>
				<td>'.$row['fix_date'].'</td>
				<td class="text-center">'.$visits_today.'</td>
				<td class="text-center">'.(int)$row['registrations'].'</td>
				<td class="text-center">'.(int)$row['countOrders'].'</td>
				<td class="text-center">'.(int)$row['countProducts'].'</td>
				<td class="text-center">'.($visits_today ? round(100 * (int)$row['registrations'] / $visits_today, 2).' %' : '-').'</td>
				<td class="text-center">'.($visits_today ? round(100 * (int)$row['countOrders'] / $visits_today, 2).' %' : '-').'</td>
				<td class="text-right">'.Tools::displayPrice($row['totalSales'], $currency).'</td>
			</tr>';

            $this->t1 += $visits_today;
            $this->t2 += (int)$row['registrations'];
            $this->t3 += (int)$row['countOrders'];
            $this->t4 += (int)$row['countProducts'];
            $this->t8 += $row['totalSales'];
        }

        $this->html .= '
				<tr>
					<th></th>
					<th class="text-center"><span class="title_box active">'.$this->trans('Visits', array(), 'Admin.Shopparameters.Feature').'</span></th>
					<th class="text-center"><span class="title_box active">'.$this->trans('Registrations', array(), 'Admin.Shopparameters.Feature').'</span></th>
					<th class="text-center"><span class="title_box active">'.$this->trans('Placed orders', array(), 'Modules.Statsforecast.Admin').'</span></th>
					<th class="text-center"><span class="title_box active">'.$this->trans('Bought items', array(), 'Modules.Statsforecast.Admin').'</span></th>
					<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of registrations', array(), 'Modules.Statsforecast.Admin').'</span></th>
					<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of orders', array(), 'Modules.Statsforecast.Admin').'</span></th>
					<th class="text-center"><span class="title_box active">'.$this->trans('Revenue', array(), 'Modules.Statsforecast.Admin').'</span></th>
				</tr>
				<tr>
					<td>'.$this->trans('Total', array(), 'Admin.Global').'</td>
					<td class="text-center">'.(int)$this->t1.'</td>
					<td class="text-center">'.(int)$this->t2.'</td>
					<td class="text-center">'.(int)$this->t3.'</td>
					<td class="text-center">'.(int)$this->t4.'</td>
					<td class="text-center">--</td>
					<td class="text-center">--</td>
					<td class="text-right">'.Tools::displayPrice($this->t8, $currency).'</td>
				</tr>
				<tr>
					<td>'.$this->trans('Average', array(), 'Modules.Statsforecast.Admin').'</td>
					<td class="text-center">'.(int)($this->t1 / $interval_avg).'</td>
					<td class="text-center">'.(int)($this->t2 / $interval_avg).'</td>
					<td class="text-center">'.(int)($this->t3 / $interval_avg).'</td>
					<td class="text-center">'.(int)($this->t4 / $interval_avg).'</td>
					<td class="text-center">'.($this->t1 ? round(100 * $this->t2 / $this->t1, 2).' %' : '-').'</td>
					<td class="text-center">'.($this->t1 ? round(100 * $this->t3 / $this->t1, 2).' %' : '-').'</td>
					<td class="text-right">'.Tools::displayPrice($this->t8 / $interval_avg, $currency).'</td>
				</tr>
				<tr>
					<td>'.$this->trans('Forecast', array(), 'Modules.Statsforecast.Admin').'</td>
					<td class="text-center">'.(int)($this->t1 * $prop30).'</td>
					<td class="text-center">'.(int)($this->t2 * $prop30).'</td>
					<td class="text-center">'.(int)($this->t3 * $prop30).'</td>
					<td class="text-center">'.(int)($this->t4 * $prop30).'</td>
					<td class="text-center">--</td>
					<td class="text-center">--</td>
					<td class="text-right">'.Tools::displayPrice($this->t8 * $prop30, $currency).'</td>
				</tr>
			</table>
		</div>';

        $ca = $this->getRealCA();

        $sql = 'SELECT COUNT(DISTINCT c.id_guest)
		FROM '._DB_PREFIX_.'connections c
		WHERE c.date_add BETWEEN '.ModuleGraph::getDateBetween().'
		'.Shop::addSqlRestriction(false, 'c');
        $visitors = Db::getInstance()->getValue($sql);

        $sql = 'SELECT COUNT(DISTINCT g.id_customer)
		FROM '._DB_PREFIX_.'connections c
		INNER JOIN '._DB_PREFIX_.'guest g ON c.id_guest = g.id_guest
		WHERE g.id_customer != 0
		AND c.date_add BETWEEN '.ModuleGraph::getDateBetween().'
		'.Shop::addSqlRestriction(false, 'c');
        $customers = Db::getInstance()->getValue($sql);

        $sql = 'SELECT COUNT(DISTINCT c.id_cart)
		FROM '._DB_PREFIX_.'cart c 
		INNER JOIN '._DB_PREFIX_.'cart_product cp on c.id_cart = cp.id_cart
		WHERE (c.date_add BETWEEN '.ModuleGraph::getDateBetween().' OR c.date_upd BETWEEN '.ModuleGraph::getDateBetween().')
		'.Shop::addSqlRestriction(false, 'c');
        $carts = Db::getInstance()->getValue($sql);

        $sql = 'SELECT COUNT(DISTINCT c.id_cart)
		FROM '._DB_PREFIX_.'cart c 
		INNER JOIN '._DB_PREFIX_.'cart_product cp on c.id_cart = cp.id_cart
		WHERE (c.date_add BETWEEN '.ModuleGraph::getDateBetween().' OR c.date_upd BETWEEN '.ModuleGraph::getDateBetween().')
		AND id_address_invoice != 0
		'.Shop::addSqlRestriction(false, 'c');
        $fullcarts = Db::getInstance()->getValue($sql);

        $sql = 'SELECT COUNT(*)
		FROM '._DB_PREFIX_.'orders o
		WHERE o.valid = 1
		AND o.date_add BETWEEN '.ModuleGraph::getDateBetween().'
		'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o');
        $orders = Db::getInstance()->getValue($sql);

        $this->html .= '
		<div class="row row-margin-bottom">
			<h4><i class="icon-filter"></i> '.$this->trans('Conversion', array(), 'Modules.Statsforecast.Admin').'</h4>
		</div>
		<div class="row row-margin-bottom">
			<table class="table">
				<tbody>
					<tr>
						<td rowspan="2" class="text-center">
							<p>'.$this->trans('Visitors', array(), 'Admin.Shopparameters.Feature').'</p>
							<p>'.$visitors.'</p>
						</td>
						<td class="text-center">
							<p><i class="icon-chevron-right"></i></p>
							<p>'.round(100 * $customers / max(1, $visitors), 2).' %</p>
						</td>
						<td class="text-center">
							<p>'.$this->trans('Accounts', array(), 'Modules.Statsforecast.Admin').'</p>
							<p>'.$customers.'</p>
						</td>
						<td class="text-center">
							<p><i class="icon-chevron-right"></i></p>
							<p>'.round(100 * $fullcarts / max(1, $customers), 2).' %</p>
						</td>
						<td rowspan="2" class="text-center">
							<p>'.$this->trans('Full carts', array(), 'Modules.Statsforecast.Admin').'</p>
							<p>'.$fullcarts.'</p>
						</td>
						<td rowspan="2" class="text-center">
							<p><i class="icon-chevron-right"></i></p>
							<p>'.round(100 * $orders / max(1, $fullcarts), 2).' %</p>
						</td>
						<td rowspan="2" class="text-center">
							<p>'.$this->trans('Orders', array(), 'Admin.Global').'</p>
							<p>'.$orders.'</p>
						</td>
						<td rowspan="2" class="text-center">
							<p>'.$this->trans('Registered visitors', array(), 'Modules.Statsforecast.Admin').'</p>
						</td>
						<td rowspan="2" class="text-center">
							<i class="icon-chevron-right"></i>
						</td>
						<td rowspan="2" class="text-center">
							<p>'.round(100 * $orders / max(1, $customers), 2).' %</p>
						</td>
						<td rowspan="2" class="text-center">
							<i class="icon-chevron-right"></i>
						</td>
						<td rowspan="2" class="text-center">
							<p>'.$this->trans('Orders', array(), 'Admin.Global').'</p>
						</td>
						<td rowspan="2" class="text-center">
							<p>'.$this->trans('Visitors', array(), 'Admin.Shopparameters.Feature').'</p>
						</td>
						<td rowspan="2" class="text-center">
							<i class="icon-chevron-right"></i>
						</td>
						<td rowspan="2" class="text-center">
							<p>'.round(100 * $orders / max(1, $visitors), 2).' %</p>
						</td>
						<td rowspan="2" class="center">
							<i class="icon-chevron-right"></i>
						</td>
						<td rowspan="2" class="text-center">
							<p>'.$this->trans('Orders', array(), 'Admin.Global').'</p>
						</td>
					</tr>
					<tr>
						<td class="text-center">
							<p><i class="icon-chevron-right"></i></p>
							<p>'.round(100 * $carts / max(1, $visitors)).' %</p>
						</td>
						<td class="text-center">
							<p>'.$this->trans('Carts', array(), 'Admin.Global').'</p>
							<p>'.$carts.'</p>
						</td>
						<td class="text-center">
							<p><i class="icon-chevron-right"></i></p>
							<p>'.round(100 * $fullcarts / max(1, $carts)).' %</p>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
		<div class="alert alert-info">
			<p>'.$this->trans('A simple statistical calculation lets you know the monetary value of your visitors:', array(), 'Modules.Statsforecast.Admin').'</p>
			<p>'.$this->trans('On average, each visitor places an order for this amount:', array(), 'Modules.Statsforecast.Admin').' <b>'.Tools::displayPrice($ca['ventil']['total'] / max(1, $visitors), $currency).'.</b></p>
			<p>'.$this->trans('On average, each registered visitor places an order for this amount:', array(), 'Modules.Statsforecast.Admin').' <b>'.Tools::displayPrice($ca['ventil']['total'] / max(1, $customers), $currency).'</b>.</p>
		</div>';

        $from = strtotime($employee->stats_date_from.' 00:00:00');
        $to = strtotime($employee->stats_date_to.' 23:59:59');
        $interval = ($to - $from) / 60 / 60 / 24;

        $this->html .= '
			<div class="row row-margin-bottom">
				<h4><i class="icon-money"></i> '.$this->trans('Payment distribution', array(), 'Modules.Statsforecast.Admin').'</h4>
				<div class="alert alert-info">'
            .$this->trans('The amounts include taxes, so you can get an estimation of the commission due to the payment method.', array(), 'Modules.Statsforecast.Admin').'
				</div>
				<form id="cat" action="'.Tools::safeOutput($ru).'#payment" method="post" class="form-horizontal">
					<div class="row row-margin-bottom">
						<label class="control-label col-lg-3">
							'.$this->trans('Zone', array(), 'Admin.Global').'
						</label>
						<div class="col-lg-3">
							<input type="hidden" name="submitIdZone" value="1" />
							<select name="stats_id_zone" onchange="this.form.submit();">
								<option value="0">'.$this->trans('-- No filter --', array(), 'Modules.Statsforecast.Admin').'</option>';
        foreach (Zone::getZones() as $zone) {
            $this->html .= '<option value="'.(int)$zone['id_zone'].'" '.($this->context->cookie->stats_id_zone == $zone['id_zone'] ? 'selected="selected"' : '').'>'.$zone['name'].'</option>';
        }
        $this->html .= '
							</select>
						</div>
					</div>
				</form>
				<table class="table">
					<thead>
						<tr>
							<th class="text-center"><span class="title_box active">'.$this->trans('Module', array(), 'Modules.Statsforecast.Admin').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Orders', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Sales', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Average cart value', array(), 'Modules.Statsforecast.Admin').'</span></th>
						</tr>
					</thead>
					<tbody>';
        foreach ($ca['payment'] as $payment) {
            $this->html .= '
						<tr>
							<td class="text-center">'.$payment['payment_method'].'</td>
							<td class="text-center">'.(int)$payment['nb'].'</td>
							<td class="text-right">'.Tools::displayPrice($payment['total'], $currency).'</td>
							<td class="text-right">'.Tools::displayPrice($payment['total'] / (int)$payment['nb'], $currency).'</td>
						</tr>';
        }
        $this->html .= '
					</tbody>
				</table>
			</div>
			<div class="row row-margin-bottom">
				<h4><i class="icon-sitemap"></i> '.$this->trans('Category distribution', array(), 'Modules.Statsforecast.Admin').'</h4>
				<form id="cat_1" action="'.Tools::safeOutput($ru).'#cat" method="post" class="form-horizontal">
					<div class="row row-margin-bottom">
						<label class="control-label col-lg-3">
							'.$this->trans('Zone', array(), 'Admin.Global').'
						</label>
						<div class="col-lg-3">
							<input type="hidden" name="submitIdZone" value="1" />
							<select name="stats_id_zone" onchange="this.form.submit();">
								<option value="0">'.$this->trans('-- No filter --', array(), 'Modules.Statsforecast.Admin').'</option>';
        foreach (Zone::getZones() as $zone) {
            $this->html .= '<option value="'.(int)$zone['id_zone'].'" '.($this->context->cookie->stats_id_zone == $zone['id_zone'] ? 'selected="selected"' : '').'>'.$zone['name'].'</option>';
        }
        $this->html .= '
							</select>
						</div>
					</div>
				</form>
				<table class="table">
					<thead>
						<tr>
							<th class="text-center"><span class="title_box active">'.$this->trans('Category', array(), 'Admin.Catalog.Feature').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Products sold', array(), 'Modules.Statsforecast.Admin').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Sales', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of products sold', array(), 'Modules.Statsforecast.Admin').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of sales', array(), 'Modules.Statsforecast.Admin').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Average price', array(), 'Admin.Global').'</span></th>
						</tr>
					</thead>
					<tbody>';
        foreach ($ca['cat'] as $catrow) {
            $this->html .= '
						<tr>
							<td class="text-center">'.(empty($catrow['name']) ? $this->trans('Unknown', array(), 'Admin.Shopparameters.Feature') : $catrow['name']).'</td>
							<td class="text-center">'.$catrow['orderQty'].'</td>
							<td class="text-right">'.Tools::displayPrice($catrow['orderSum'], $currency).'</td>
							<td class="text-center">'.number_format((100 * $catrow['orderQty'] / $this->t4), 1, '.', ' ').'%</td>
							<td class="text-center">'.((int)$ca['ventil']['total'] ? number_format((100 * $catrow['orderSum'] / $ca['ventil']['total']), 1, '.', ' ') : '0').'%</td>
							<td class="text-right">'.Tools::displayPrice($catrow['priveAvg'], $currency).'</td>
						</tr>';
        }
        $this->html .= '
					</tbody>
				</table>
			</div>
			<div class="row row-margin-bottom">
				<h4><i class="icon-flag"></i> '.$this->trans('Language distribution', array(), 'Modules.Statsforecast.Admin').'</h4>
				<table class="table">
					<thead>
						<tr>
							<th class="text-center"><span class="title_box active">'.$this->trans('Language', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Sales', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Percentage', array(), 'Admin.Global').'</span></th>
							<th class="text-center" colspan="2"><span class="title_box active">'.$this->trans('Growth', array(), 'Modules.Statsforecast.Admin').'</span></th>
						</tr>
					</thead>
					<tbody>';
        foreach ($ca['lang'] as $ophone => $amount) {
            $percent = (int)($ca['langprev'][$ophone]) ? number_format((100 * $amount / $ca['langprev'][$ophone]) - 100, 1, '.', ' ') : '&#x221e;';
            $this->html .= '
					<tr '.(($percent < 0) ? 'class="alt_row"' : '').'>
						<td class="text-center">'.$ophone.'</td>
						<td class="text-right">'.Tools::displayPrice($amount, $currency).'</td>
						<td class="text-center">'.((int)$ca['ventil']['total'] ? number_format((100 * $amount / $ca['ventil']['total']), 1, '.', ' ').'%' : '-').'</td>
						<td class="text-center">'.(($percent > 0 || $percent == '&#x221e;') ? '<img src="../img/admin/arrow_up.png" alt="" />' : '<img src="../img/admin/arrow_down.png" alt="" /> ').'</td>
						<td class="text-center">'.(($percent > 0 || $percent == '&#x221e;') ? '+' : '').$percent.'%</td>
					</tr>';
        }
        $this->html .= '
					</tbody>
				</table>
			</div>
			<div class="row row-margin-bottom">
				<h4><i class="icon-map-marker"></i> '.$this->trans('Zone distribution', array(), 'Modules.Statsforecast.Admin').'</h4>
				<table class="table">
					<thead>
						<tr>
							<th class="text-center"><span class="title_box active">'.$this->trans('Zone', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Orders', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Sales', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of orders', array(), 'Modules.Statsforecast.Admin').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of sales', array(), 'Modules.Statsforecast.Admin').'</span></th>
						</tr>
					</thead>
					<tbody>';
        foreach ($ca['zones'] as $zone) {
            $this->html .= '
					<tr>
						<td class="text-center">'.(isset($zone['name']) ? $zone['name'] : $this->trans('Undefined', array(), 'Admin.Shopparameters.Feature')).'</td>
						<td class="text-center">'.(int)($zone['nb']).'</td>
						<td class="text-right">'.Tools::displayPrice($zone['total'], $currency).'</td>
						<td class="text-center">'.($ca['ventil']['nb'] ? number_format((100 * $zone['nb'] / $ca['ventil']['nb']), 1, '.', ' ') : '0').'%</td>
						<td class="text-center">'.((int)$ca['ventil']['total'] ? number_format((100 * $zone['total'] / $ca['ventil']['total']), 1, '.', ' ') : '0').'%</td>
					</tr>';
        }
        $this->html .= '
					</tbody>
				</table>
			</div>
			<div class="row row-margin-bottom">
				<h4><i class="icon-money"></i> '.$this->trans('Currency distribution', array(), 'Modules.Statsforecast.Admin').'</h4>
				<form id="cat_2" action="'.Tools::safeOutput($ru).'#currencies" method="post" class="form-horizontal">
					<div class="row row-margin-bottom">
						<label class="control-label col-lg-3">
							'.$this->trans('Zone', array(), 'Admin.Global').'
						</label>
						<div class="col-lg-3">
							<input type="hidden" name="submitIdZone" value="1" />
							<select name="stats_id_zone" onchange="this.form.submit();">
								<option value="0">'.$this->trans('-- No filter --', array(), 'Modules.Statsforecast.Admin').'</option>';
        foreach (Zone::getZones() as $zone) {
            $this->html .= '<option value="'.(int)$zone['id_zone'].'" '.($this->context->cookie->stats_id_zone == $zone['id_zone'] ? 'selected="selected"' : '').'>'.$zone['name'].'</option>';
        }
        $this->html .= '
							</select>
						</div>
					</div>
				</form>
				<table class="table">
					<thead>
						<tr>
							<th class="text-center"><span class="title_box active">'.$this->trans('Currency', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Orders', array(), 'Admin.Global').'</span></th>
							<th class="text-right"><span class="title_box active">'.$this->trans('Sales (converted)', array(), 'Modules.Statsforecast.Admin').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of orders', array(), 'Modules.Statsforecast.Admin').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Percentage of sales', array(), 'Modules.Statsforecast.Admin').'</span></th>
						</tr>
					</thead>
					<tbody>';
        foreach ($ca['currencies'] as $currency_row) {
            $this->html .= '
						<tr>
							<td class="text-center">'.$currency_row['name'].'</td>
							<td class="text-center">'.(int)($currency_row['nb']).'</td>
							<td class="text-right">'.Tools::displayPrice($currency_row['total'], $currency).'</td>
							<td class="text-center">'.($ca['ventil']['nb'] ? number_format((100 * $currency_row['nb'] / $ca['ventil']['nb']), 1, '.', ' ') : '0').'%</td>
							<td class="text-center">'.((int)$ca['ventil']['total'] ? number_format((100 * $currency_row['total'] / $ca['ventil']['total']), 1, '.', ' ') : '0').'%</td>
						</tr>';
        }
        $this->html .= '
					</tbody>
				</table>
			</div>
			<div class="row row-margin-bottom">
				<h4><i class="icon-ticket"></i> '.$this->trans('Attribute distribution', array(), 'Modules.Statsforecast.Admin').'</h4>
				<table class="table">
					<thead>
						<tr>
							<th class="text-center"><span class="title_box active">'.$this->trans('Group', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Attribute', array(), 'Admin.Global').'</span></th>
							<th class="text-center"><span class="title_box active">'.$this->trans('Quantity of products sold', array(), 'Modules.Statsforecast.Admin').'</span></th>
						</tr>
					</thead>
					<tbody>';
        foreach ($ca['attributes'] as $attribut) {
            $this->html .= '
						<tr>
							<td class="text-center">'.$attribut['gname'].'</td>
							<td class="text-center">'.$attribut['aname'].'</td>
							<td class="text-center">'.(int)($attribut['total']).'</td>
						</tr>';
        }
        $this->html .= '
					</tbody>
				</table>
			</div>';

        return $this->html;
    }

    private function getRealCA()
    {
        $employee = $this->context->employee;
        $ca = array();

        $where = $join = '';
        if ((int)$this->context->cookie->stats_id_zone) {
            $join = ' LEFT JOIN `'._DB_PREFIX_.'address` a ON o.id_address_invoice = a.id_address LEFT JOIN `'._DB_PREFIX_.'country` co ON co.id_country = a.id_country';
            $where = ' AND co.id_zone = '.(int)$this->context->cookie->stats_id_zone.' ';
        }

        $sql = 'SELECT SUM(od.`product_price` * od.`product_quantity` / o.conversion_rate) as orderSum, SUM(od.product_quantity) as orderQty, cl.name, AVG(od.`product_price` / o.conversion_rate) as priveAvg
				FROM `'._DB_PREFIX_.'orders` o
				STRAIGHT_JOIN `'._DB_PREFIX_.'order_detail` od ON o.id_order = od.id_order
				LEFT JOIN `'._DB_PREFIX_.'product` p ON p.id_product = od.product_id
				'.Shop::addSqlAssociation('product', 'p').'
				LEFT JOIN `'._DB_PREFIX_.'category_lang` cl ON (product_shop.id_category_default = cl.id_category AND cl.id_lang = '.(int)$this->context->language->id.Shop::addSqlRestrictionOnLang('cl').')
				'.$join.'
				WHERE o.valid = 1
					AND o.`invoice_date` BETWEEN '.ModuleGraph::getDateBetween().'
					'.$where.'
					'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o').'
				GROUP BY product_shop.id_category_default';
        $ca['cat'] = Db::getInstance()->executeS($sql);
        uasort($ca['cat'], 'statsforecast_sort');

        $lang_values = '';
        $sql = 'SELECT l.id_lang, l.iso_code
				FROM `'._DB_PREFIX_.'lang` l
				'.Shop::addSqlAssociation('lang', 'l').'
				WHERE l.active = 1';
        $languages = Db::getInstance()->executeS($sql);
        foreach ($languages as $language) {
            $lang_values .= 'SUM(IF(o.id_lang = '.(int)$language['id_lang'].', total_paid_tax_excl / o.conversion_rate, 0)) as '.pSQL($language['iso_code']).',';
        }
        $lang_values = rtrim($lang_values, ',');

        if ($lang_values) {
            $sql = 'SELECT '.$lang_values.'
					FROM `'._DB_PREFIX_.'orders` o
					WHERE o.valid = 1
					AND o.`invoice_date` BETWEEN '.ModuleGraph::getDateBetween().'
					'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o');
            $ca['lang'] = Db::getInstance()->getRow($sql);
            arsort($ca['lang']);

            $sql = 'SELECT '.$lang_values.'
					FROM `'._DB_PREFIX_.'orders` o
					WHERE o.valid = 1
						AND ADDDATE(o.`invoice_date`, interval 30 day) BETWEEN \''.$employee->stats_date_from.' 00:00:00\' AND \''.min(date('Y-m-d H:i:s'), $employee->stats_date_to.' 23:59:59').'\'
						'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o');
            $ca['langprev'] = Db::getInstance()->getRow($sql);
        } else {
            $ca['lang'] = array();
            $ca['langprev'] = array();
        }

        $sql = 'SELECT reference
					FROM `'._DB_PREFIX_.'orders` o
					'.$join.'
					WHERE o.valid
					'.$where.'
					'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o').'
					AND o.invoice_date BETWEEN '.ModuleGraph::getDateBetween().'';
        $result = Db::getInstance()->executeS($sql);
        if (count($result)) {
            $references = array();
            foreach ($result as $r) {
                $references[] = $r['reference'];
            }
            $sql = 'SELECT op.payment_method, SUM(op.amount / op.conversion_rate) as total, COUNT(DISTINCT op.order_reference) as nb
					FROM `'._DB_PREFIX_.'order_payment` op
					WHERE op.`date_add` BETWEEN '.ModuleGraph::getDateBetween().'
					AND op.order_reference IN (
						"'.implode('","', $references).'"
					)
					GROUP BY op.payment_method
					ORDER BY total DESC';
            $ca['payment'] = Db::getInstance()->executeS($sql);
        } else {
            $ca['payment'] = array();
        }

        $sql = 'SELECT z.name, SUM(o.total_paid_tax_excl / o.conversion_rate) as total, COUNT(*) as nb
				FROM `'._DB_PREFIX_.'orders` o
				LEFT JOIN `'._DB_PREFIX_.'address` a ON o.id_address_invoice = a.id_address
				LEFT JOIN `'._DB_PREFIX_.'country` c ON c.id_country = a.id_country
				LEFT JOIN `'._DB_PREFIX_.'zone` z ON z.id_zone = c.id_zone
				WHERE o.valid = 1
					AND o.`invoice_date` BETWEEN '.ModuleGraph::getDateBetween().'
					'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o').'
				GROUP BY c.id_zone
				ORDER BY total DESC';
        $ca['zones'] = Db::getInstance()->executeS($sql);

        $sql = 'SELECT cu.name, SUM(o.total_paid_tax_excl / o.conversion_rate) as total, COUNT(*) as nb
				FROM `'._DB_PREFIX_.'orders` o
				LEFT JOIN `'._DB_PREFIX_.'currency` cu ON o.id_currency = cu.id_currency
				'.$join.'
				WHERE o.valid = 1
					AND o.`invoice_date` BETWEEN '.ModuleGraph::getDateBetween().'
					'.$where.'
					'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o').'
				GROUP BY o.id_currency
				ORDER BY total DESC';
        $ca['currencies'] = Db::getInstance()->executeS($sql);

        $sql = 'SELECT SUM(total_paid_tax_excl / o.conversion_rate) as total, COUNT(*) AS nb
				FROM `'._DB_PREFIX_.'orders` o
				WHERE o.valid = 1
					AND o.`invoice_date` BETWEEN '.ModuleGraph::getDateBetween().'
					'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o');
        $ca['ventil'] = Db::getInstance()->getRow($sql);

        $sql = 'SELECT /*pac.id_attribute,*/ agl.name as gname, al.name as aname, COUNT(*) as total
				FROM '._DB_PREFIX_.'orders o
				LEFT JOIN '._DB_PREFIX_.'order_detail od ON o.id_order = od.id_order
				INNER JOIN '._DB_PREFIX_.'product_attribute_combination pac ON od.product_attribute_id = pac.id_product_attribute
				INNER JOIN '._DB_PREFIX_.'attribute a ON pac.id_attribute = a.id_attribute
				INNER JOIN '._DB_PREFIX_.'attribute_group_lang agl ON (a.id_attribute_group = agl.id_attribute_group AND agl.id_lang = '.(int)$this->context->language->id.')
				INNER JOIN '._DB_PREFIX_.'attribute_lang al ON (a.id_attribute = al.id_attribute AND al.id_lang = '.(int)$this->context->language->id.')
				WHERE o.valid = 1
					AND o.`invoice_date` BETWEEN '.ModuleGraph::getDateBetween().'
					'.Shop::addSqlRestriction(Shop::SHARE_ORDER, 'o').'
				GROUP BY pac.id_attribute';
        $ca['attributes'] = Db::getInstance()->executeS($sql);

        return $ca;
    }
}

function statsforecast_sort($a, $b)
{
    if ($a['orderSum'] == $b['orderSum']) {
        return 0;
    }

    return ($a['orderSum'] > $b['orderSum']) ? -1 : 1;
}
