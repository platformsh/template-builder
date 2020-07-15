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

use PrestaShop\PrestaShop\Core\Module\WidgetInterface;

if (!defined('_PS_VERSION_')) {
    exit;
}

class Ps_CustomerSignIn extends Module implements WidgetInterface
{
    private $templateFile;

    public function __construct()
    {
        $this->name = 'ps_customersignin';
        $this->author = 'PrestaShop';
        $this->version = '2.0.2';
        $this->need_instance = 0;

        parent::__construct();

        $this->displayName = $this->getTranslator()->trans('Customer "Sign in" link', array(), 'Modules.Customersignin.Admin');
        $this->description = $this->getTranslator()->trans('Adds a block that displays information about the customer.', array(), 'Modules.Customersignin.Admin');
        $this->ps_versions_compliancy = array('min' => '1.7.1.0', 'max' => _PS_VERSION_);

        $this->templateFile = 'module:ps_customersignin/ps_customersignin.tpl';
    }

    public function getWidgetVariables($hookName, array $configuration)
    {
        $logged = $this->context->customer->isLogged();

        if ($logged) {
            $customerName = $this->getTranslator()->trans(
                '%firstname% %lastname%',
                array(
                    '%firstname%' => $this->context->customer->firstname,
                    '%lastname%' => $this->context->customer->lastname,
                ),
                'Modules.Customersignin.Admin'
            );
        } else {
            $customerName = '';
        }

        $link = $this->context->link;

        return array(
            'logged' => $logged,
            'customerName' => $customerName,
            'logout_url' => $link->getPageLink('index', true, null, 'mylogout'),
            'my_account_url' => $link->getPageLink('my-account', true),

        );
    }

    public function renderWidget($hookName, array $configuration)
    {
        $this->smarty->assign($this->getWidgetVariables($hookName, $configuration));
        return $this->fetch($this->templateFile);
    }
}
