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

use PrestaShop\PrestaShop\Core\Module\WidgetInterface;

class Ps_Searchbar extends Module implements WidgetInterface
{
    private $templateFile;

    public function __construct()
    {
        $this->name = 'ps_searchbar';
        $this->author = 'PrestaShop';
        $this->version = '2.0.1';
        $this->need_instance = 0;

        parent::__construct();

        $this->displayName = $this->trans('Search bar', array(), 'Modules.Searchbar.Admin');
        $this->description = $this->trans('Adds a quick search field to your website.', array(), 'Modules.Searchbar.Admin');

        $this->ps_versions_compliancy = array('min' => '1.7.1.0', 'max' => _PS_VERSION_);

        $this->templateFile = 'module:ps_searchbar/ps_searchbar.tpl';
    }

    public function install()
    {
        return parent::install()
            && $this->registerHook('top')
            && $this->registerHook('displaySearch')
            && $this->registerHook('header')
        ;
    }

    public function hookHeader()
    {
        $this->context->controller->addJqueryUI('ui.autocomplete');
        $this->context->controller->registerJavascript('modules-searchbar', 'modules/'.$this->name.'/ps_searchbar.js', ['position' => 'bottom', 'priority' => 150]);
    }

    public function getWidgetVariables($hookName, array $configuration = [])
    {
        $widgetVariables = array(
            'search_controller_url' => $this->context->link->getPageLink('search', null, null, null, false, null, true),
        );

        if (!array_key_exists('search_string', $this->context->smarty->getTemplateVars())) {
            $widgetVariables['search_string'] = '';
        }

        return $widgetVariables;
    }

    public function renderWidget($hookName, array $configuration = [])
    {
        $this->smarty->assign($this->getWidgetVariables($hookName, $configuration));

        return $this->fetch($this->templateFile);
    }
}
