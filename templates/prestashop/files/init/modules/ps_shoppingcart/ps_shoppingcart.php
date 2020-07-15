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

use PrestaShop\PrestaShop\Adapter\Cart\CartPresenter;

if (!defined('_PS_VERSION_')) {
    exit;
}

use PrestaShop\PrestaShop\Core\Module\WidgetInterface;

class Ps_Shoppingcart extends Module implements WidgetInterface
{
    public function __construct()
    {
        $this->name = 'ps_shoppingcart';
        $this->tab = 'front_office_features';
        $this->version = '2.0.2';
        $this->author = 'PrestaShop';
        $this->need_instance = 0;

        $this->bootstrap = true;
        parent::__construct();

        $this->displayName = $this->trans('Shopping cart', array(), 'Modules.Shoppingcart.Admin');
        $this->description = $this->trans('Adds a block containing the customer\'s shopping cart.', array(), 'Modules.Shoppingcart.Admin');
        $this->ps_versions_compliancy = array('min' => '1.7.1.0', 'max' => _PS_VERSION_);
        $this->controllers = array('ajax');
    }

    public function hookHeader()
    {
        if (Configuration::isCatalogMode()) {
            return;
        }

        if (Configuration::get('PS_BLOCK_CART_AJAX')) {
            $this->context->controller->registerJavascript('modules-shoppingcart', 'modules/'.$this->name.'/ps_shoppingcart.js', ['position' => 'bottom', 'priority' => 150]);
        }
    }

    private function getCartSummaryURL()
    {
        return $this->context->link->getPageLink(
            'cart',
            null,
            $this->context->language->id,
            array(
                'action' => 'show'
            ),
            false,
            null,
            true
        );
    }

    public function getWidgetVariables($hookName, array $params)
    {
        $cart_url = $this->getCartSummaryURL();

        return array(
            'cart' => (new CartPresenter)->present(isset($params['cart']) ? $params['cart'] : $this->context->cart),
            'refresh_url' => $this->context->link->getModuleLink('ps_shoppingcart', 'ajax', array(), null, null, null, true),
            'cart_url' => $cart_url
        );
    }

    public function renderWidget($hookName, array $params)
    {
        if (Configuration::isCatalogMode()) {
            return;
        }

        $this->smarty->assign($this->getWidgetVariables($hookName, $params));
        return $this->fetch('module:ps_shoppingcart/ps_shoppingcart.tpl');
    }

    public function renderModal(Cart $cart, $id_product, $id_product_attribute)
    {
        $data = (new CartPresenter)->present($cart);
        $product = null;
        foreach ($data['products'] as $p) {
            if ($p['id_product'] == $id_product && $p['id_product_attribute'] == $id_product_attribute) {
                $product = $p;
                break;
            }
        }

        $this->smarty->assign(array(
            'product' => $product,
            'cart' => $data,
            'cart_url' => $this->getCartSummaryURL(),
        ));

        return $this->fetch('module:ps_shoppingcart/modal.tpl');
    }

    public function getContent()
    {
        $output = '';
        if (Tools::isSubmit('submitBlockCart')) {
            $ajax = Tools::getValue('PS_BLOCK_CART_AJAX');
            if ($ajax != 0 && $ajax != 1) {
                $output .= $this->displayError($this->trans('Ajax: Invalid choice.', array(), 'Modules.Shoppingcart.Admin'));
            } else {
                Configuration::updateValue('PS_BLOCK_CART_AJAX', (int)($ajax));
            }
        }
        return $output.$this->renderForm();
    }

    public function install()
    {
        return
            parent::install()
                && $this->registerHook('header')
                && $this->registerHook('displayTop')
                && Configuration::updateValue('PS_BLOCK_CART_AJAX', 1)
        ;
    }

    public function renderForm()
    {
        $fields_form = array(
            'form' => array(
                'legend' => array(
                    'title' => $this->trans('Settings', array(), 'Admin.Global'),
                    'icon' => 'icon-cogs',
                ),
                'input' => array(
                    array(
                        'type' => 'switch',
                        'label' => $this->trans('Ajax cart', array(), 'Modules.Shoppingcart.Admin'),
                        'name' => 'PS_BLOCK_CART_AJAX',
                        'is_bool' => true,
                        'desc' => $this->trans('Activate Ajax mode for the cart (compatible with the default theme).', array(), 'Modules.Shoppingcart.Admin'),
                        'values' => array(
                            array(
                                'id' => 'active_on',
                                'value' => 1,
                                'label' => $this->trans('Enabled', array(), 'Admin.Global'),
                            ),
                            array(
                                'id' => 'active_off',
                                'value' => 0,
                                'label' => $this->trans('Disabled', array(), 'Admin.Global'),
                            )
                        ),
                    ),
                ),
                'submit' => array(
                    'title' => $this->trans('Save', array(), 'Admin.Actions'),
                ),
            ),
        );

        $helper = new HelperForm();
        $helper->show_toolbar = false;
        $helper->table =  $this->table;
        $lang = new Language((int)Configuration::get('PS_LANG_DEFAULT'));
        $helper->default_form_language = $lang->id;
        $helper->allow_employee_form_lang = Configuration::get('PS_BO_ALLOW_EMPLOYEE_FORM_LANG') ? Configuration::get('PS_BO_ALLOW_EMPLOYEE_FORM_LANG') : 0;
        $this->fields_form = array();

        $helper->identifier = $this->identifier;
        $helper->submit_action = 'submitBlockCart';
        $helper->currentIndex = $this->context->link->getAdminLink('AdminModules', false).'&configure='.$this->name.'&tab_module='.$this->tab
        .'&module_name='.$this->name;
        $helper->token = Tools::getAdminTokenLite('AdminModules');
        $helper->tpl_vars = array(
            'fields_value' => $this->getConfigFieldsValues(),
            'languages' => $this->context->controller->getLanguages(),
            'id_language' => $this->context->language->id
        );

        return $helper->generateForm(array($fields_form));
    }

    public function getConfigFieldsValues()
    {
        return array(
            'PS_BLOCK_CART_AJAX' => (bool)Tools::getValue('PS_BLOCK_CART_AJAX', Configuration::get('PS_BLOCK_CART_AJAX')),
        );
    }
}
