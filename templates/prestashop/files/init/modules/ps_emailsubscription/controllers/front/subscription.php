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

/**
 * @since 1.5.0
 */
class Ps_EmailsubscriptionSubscriptionModuleFrontController extends ModuleFrontController
{
    private $variables = [];

    /**
     * @see FrontController::postProcess()
     */
    public function postProcess()
    {

        $this->variables['value'] = Tools::getValue('email', '');
        $this->variables['msg'] = '';
        $this->variables['conditions'] = Configuration::get('NW_CONDITIONS', $this->context->language->id);

        if (Tools::isSubmit('submitNewsletter')) {
            $this->module->newsletterRegistration();
            if ($this->module->error) {
                $this->variables['msg'] = $this->module->error;
                $this->variables['nw_error'] = true;
            } elseif ($this->module->valid) {
                $this->variables['msg'] = $this->module->valid;
                $this->variables['nw_error'] = false;
            }
        }

    }

    /**
     * @see FrontController::initContent()
     */
    public function initContent()
    {
        parent::initContent();

        $this->context->smarty->assign('variables', $this->variables);
        $this->setTemplate('module:ps_emailsubscription/views/templates/front/subscription_execution.tpl');
    }
}
