<?php
/**
* 2007-2018 PrestaShop
*
* NOTICE OF LICENSE
*
* This source file is subject to the Open Software License (OSL 3.0)
* that is bundled with this package in the file LICENSE.txt.
* It is also available through the world-wide-web at this URL:
* http://opensource.org/licenses/osl-3.0.php
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
* @author PrestaShop SA <contact@prestashop.com>
* @copyright 2007-2018 PrestaShop SA
* @license http://opensource.org/licenses/osl-3.0.php Open Software License (OSL 3.0)
* International Registered Trademark & Property of PrestaShop SA
**/

require_once(dirname(__FILE__).'../../../classes/ThemeCustoRequests.php');

class AdminPsThemeCustoConfigurationController extends ModuleAdminController
{
    public function __construct()
    {
        parent::__construct();

        $this->controller_quick_name = 'configuration';
        $this->aModuleActions = array('uninstall', 'install', 'configure', 'enable', 'disable', 'disable_mobile', 'enable_mobile', 'reset' );
        $this->moduleActionsNames = array(
            $this->l('Uninstall'),
            $this->l('Install'),
            $this->l('Configure'),
            $this->l('Enable'),
            $this->l('Disable'),
            $this->l('Disable Mobile'),
            $this->l('Enable Mobile'),
            $this->l('Reset')
        );
        $this->categoryList = array(
            'menu'              => $this->l('Menu'),
            'slider'            => $this->l('Slider'),
            'home_products'     => $this->l('Home Products'),
            'block_text'        => $this->l('Text block'),
            'banner'            => $this->l('Banner'),
            'social_newsletter' => $this->l('Social &  Newsletter'),
            'footer'            => $this->l('Footer')
        );
    }

    /**
     * Get modules list to show
     *
     * @param none
     * @return array $aList
    */
    public function getListToConfigure()
    {
        $aList = array(
            'menu' => array(
                'pages' => array(
                    'AdminCategories' => array(
                        $this->l('Create and manage Product Categories'),
                        $this->l('Create here a full range of categories and subcategories to classify your products and manage your catalog easily.')
                    ),
                    'AdminCmsContent' => array(
                        $this->l('Create content pages'),
                        $this->l('Add and manage your content pages (CMS pages: Terms and conditions of use, Our stores, About us, etc.) as you want.')
                    ),
                    'AdminManufacturers' => array(
                        $this->l('Create Brands and Suppliers pages'),
                        $this->l('This page allows you to create and manage your Brands and/or Suppliers pages.')
                    ),
                ),
                'modules' => array(
                    'ps_mainmenu' => 22321,
                ),
            ),
            'slider' => array(
                'modules' => array(
                    (($this->module->ready)? 'pshomeslider' : 'ps_imageslider') => (($this->module->ready)? 27562 : 22320)
                ),
            ),
            'home_products' => array(
                'modules' => array(
                    'ps_featuredproducts' => 22319,
                    'ps_bestsellers' => 24566,
                    'ps_newproducts' => 24671,
                    'ps_specials' => 24672,

                ),
            ),
            'block_text' => array(
                'modules' => array(
                    'ps_customtext' => 22317,
                ),
            ),
            'banner' => array(
                'modules' => array(
                    'ps_banner' => 22313,
                ),
            ),
            'social_newsletter' => array(
                'modules' => array(
                    'ps_emailsubscription'  => 22318,
                    'ps_socialfollow' => 22323,
                ),
            ),
            'footer' => array(
                'pages' => array(
                    'AdminStores' => array(
                        $this->l('Shop details'),
                        $this->l('Display additional information about your store or how to contact you to make it easy for your customers to reach you.')
                    ),
                ),
                'modules' => array(
                    'ps_linklist' => 24360
                ),
            ),
        );

        return $aList;
    }

    /**
     * Initialize the content by adding Boostrap and loading the TPL
     *
     * @param none
     * @return none
    */
    public function initContent()
    {
        parent::initContent();

        if (Module::isInstalled('ps_mbo')) {
            $selectionModulePage = $this->context->link->getAdminLink('AdminPsMboModule');
        } else {
            $selectionModulePage = $this->context->link->getAdminLink('AdminModulesCatalog');
        }
        $installedModulePage = $this->context->link->getAdminLink('AdminModulesManage');

        $aListToConfigure = $this->getListToConfigure();
        $this->context->smarty->assign(array(
            'enable'                => $this->module->active,
            'moduleName'            => $this->module->displayName,
            'bootstrap'             => 1,
            'configure_type'        => $this->controller_quick_name,
            'iconConfiguration'     => $this->module->img_path.'/controllers/configuration/icon_configurator.png',
            'listCategories'        => $this->categoryList,
            'elementsList'          => $this->setFinalList($aListToConfigure),
            'selectionModulePage'   => $selectionModulePage,
            'installedModulePage'   => $installedModulePage,
            'moduleImgUri'          => $this->module->img_path.'/controllers/configuration/',
            'moduleActions'         => $this->aModuleActions,
            'moduleActionsNames'    => $this->moduleActionsNames,
            'themeConfiguratorUrl'  => $this->context->link->getAdminLink('AdminModules', true, false, array('configure' => 'ps_themeconfigurator')),
            'is_ps_ready'           => $this->module->ready,
            'ps_uri'                => $this->module->ps_uri
        ));

        $aJsDef = array(
            'admin_module_controller_psthemecusto'  => $this->module->controller_name[1],
            'admin_module_ajax_url_psthemecusto'    => $this->module->front_controller[1],
            'module_action_sucess'                  => $this->l('Action on the module successfully completed'),
            'module_action_failed'                  => $this->l('Action on module failed'),
        );
        $aJs = array($this->module->js_path.'/controllers/'.$this->controller_quick_name.'/back.js');
        $aCss = array($this->module->css_path.'/controllers/'.$this->controller_quick_name.'/back.css');

        $this->module->setMedia($aJsDef, $aJs, $aCss);
        $this->setTemplate( $this->module->template_dir.'page.tpl');
    }


    /**
     * AJAX : Do a module action like Install, disable, enable ...
     *
     * @param null
     * @return mixed int | tpl
    */
    public function ajaxProcessUpdateModule()
    {
        if (!$this->module->hasEditRight()) {
            die($this->l('You do not have permission to edit this.'));
        }

        $iModuleId      = (int)Tools::getValue('id_module');
        $sModuleName    = pSQL(Tools::getValue('module_name'));
        $sModuleAction  = pSQL(Tools::getValue('action_module'));
        $oModule        = Module::getInstanceByName($sModuleName);
        $bReturn        = false;
        $sUrlActive     = ($oModule->isEnabled($oModule->name)? 'configure' : 'enable');

        switch ($sModuleAction) {
            case 'uninstall':
                if ($this->module->ready === true) {
                    break;
                }
                $bReturn = $oModule->uninstall();
                $sUrlActive = 'install';
            break;
            case 'install':
                if ($this->module->ready === true) {
                    break;
                }
                $bReturn = $oModule->install();
                $sUrlActive = (method_exists($oModule, 'getContent'))? 'configure' : 'disable';
            break;
            case 'enable':
                $bReturn = $oModule->enable();
                $sUrlActive = (method_exists($oModule, 'getContent'))? 'configure' : 'disable';
            break;
            case 'disable':
                $bReturn = $oModule->disable();
                $sUrlActive = 'enable';
            break;
            case 'disable_mobile':
                $bReturn = $oModule->disableDevice(Context::DEVICE_MOBILE);
                $sUrlActive = (method_exists($oModule, 'getContent'))? 'configure' : 'disable';
            break;
            case 'enable_mobile':
                $bReturn = $oModule->enableDevice(Context::DEVICE_MOBILE);
                $sUrlActive = (method_exists($oModule, 'getContent'))? 'configure' : 'disable';
            break;
            case 'reset':
                $bReturn = $oModule->uninstall();
                $bReturn = $oModule->install();
                $sUrlActive = (method_exists($oModule, 'getContent'))? 'configure' : 'disable';
            break;
            default:
                die(0);
            break;
        }

        $aModule['id_module'] = $oModule->id;
        $aModule['name'] = $oModule->name;
        $aModule['displayName'] = $oModule->displayName;
        $aModule['url_active'] = $sUrlActive;
        $aModule['active'] = ThemeCustoRequests::getModuleDeviceStatus($oModule->id);
        $aModule['actions_url']['configure'] = $this->context->link->getAdminLink('AdminModules', true, false, array('configure' => $oModule->name));
        $aModule['can_configure'] = (method_exists($oModule, 'getContent'))? true : false;
        $aModule['enable_mobile'] = (int)Db::getInstance()->getValue('SELECT enable_device FROM '._DB_PREFIX_.'module_shop WHERE id_module = '.(int)$oModule->id);

        unset($oModule);

        $this->context->smarty->assign(array(
            'module'                => $aModule,
            'moduleActions'         => $this->aModuleActions,
            'moduleActionsNames'    => $this->moduleActionsNames,
            'is_ps_ready'           => $this->module->ready,
            )
        );

        die($this->context->smarty->fetch(dirname(__FILE__).'/../../views/templates/admin/controllers/'.$this->controller_quick_name.'/elem/module_actions.tpl'));
    }

    /**
     * get list to show
     *
     * @param array $aList
     * @return none
    */
    public function setFinalList($aList)
    {
        $modulesOnDisk = Module::getModulesDirOnDisk();
        $aModuleFinalList = array();

        foreach ($aList as $sSegmentName => $aElementListByType) {
            foreach ($aElementListByType as $sType => $aElementsList) {
                if ($sType == 'pages') {
                    foreach ($aElementsList as $sController => $aPage) {
                        $aModuleFinalList[$sSegmentName][$sType][$sController]['displayName'] = $this->l($aPage[0]);
                        $aModuleFinalList[$sSegmentName][$sType][$sController]['url'] = $this->context->link->getAdminLink($sController);
                        $aModuleFinalList[$sSegmentName][$sType][$sController]['description'] = $this->l($aPage[1]);
                        $aModuleFinalList[$sSegmentName][$sType][$sController]['action'] = $this->l('Configure');
                    }
                } else {
                    foreach ($aElementsList as $sModuleName => $iModuleId) {
                        if (!in_array($sModuleName, $modulesOnDisk)) {
                            if ($this->module->ready !== false) {
                                continue;
                            }
                            /* For a module coming from outside. It will be downloaded and installed */
                            $length = file_put_contents(_PS_MODULE_DIR_.basename($sModuleName).'.zip', Tools::addonsRequest('module', array('id_module' => $iModuleId)));
                            if (!empty($length) && Tools::ZipExtract(_PS_MODULE_DIR_.basename($sModuleName).'.zip', _PS_MODULE_DIR_)) {
                                @unlink(_PS_MODULE_DIR_.basename($sModuleName).'.zip');
                            } else {
                                continue;
                            }
                        }

                        $aModuleFinalList[$sSegmentName][$sType][$sModuleName] = $this->setModuleFinalList(Module::getInstanceByName($sModuleName), Module::isInstalled($sModuleName));
                    }
                }
            }
            if (!isset($aModuleFinalList[$sSegmentName])) {
                $aModuleFinalList[$sSegmentName] = null;
            }
            if (is_array($aModuleFinalList[$sSegmentName]['modules'])) {
                uasort($aModuleFinalList[$sSegmentName]['modules'], array($this, 'sortArrayInstalledModulesFirst'));
            }
        }

        return $aModuleFinalList;
    }

    /**
     * Render final list of modules
     *
     * @param object $oModuleInstance
     * @param bool $bIsInstalled
     * @return array $aModule
    */
    public function setModuleFinalList($oModuleInstance, $bIsInstalled)
    {
        $aModule = array();

        $aModule['id_module'] = $oModuleInstance->id;
        $aModule['active'] = $oModuleInstance->active;



        if ($bIsInstalled === true) {
            $aModule['can_configure'] = (method_exists($oModuleInstance, 'getContent'))? true : false;
            if (method_exists($oModuleInstance, 'getContent')) {
                $aModule['url_active'] = $this->l(($oModuleInstance->active? 'configure' : 'enable'));
            } else {
                $aModule['url_active'] = $this->l(($oModuleInstance->active? 'disable' : 'enable'));
            }
            $aModule['installed'] = 1;
        } else {
            $aModule['can_configure'] = false;
            $aModule['url_active'] = 'install';
            $aModule['installed'] = 0;
        }

        $aModule['enable_mobile'] = (int)Db::getInstance()->getValue('SELECT enable_device FROM '._DB_PREFIX_.'module_shop WHERE id_module = '.(int)$oModuleInstance->id);
        $aModule['name'] = $oModuleInstance->name;
        $aModule['displayName'] = $oModuleInstance->displayName;
        $aModule['description'] = $oModuleInstance->description;
        $aModule['controller_name'] = (isset($oModuleInstance->controller_name)? $oModuleInstance->controller_name : '');
        $aModule['logo'] = '/modules/'.$oModuleInstance->name.'/logo.png';
        $aModule['actions_url']['configure'] = $this->context->link->getAdminLink('AdminModules', true, false, array('configure' => $oModuleInstance->name));

        return $aModule;
    }

    /**
     * Order Final array for having installed module first
     *
     * @param array $a
     * @param array $b
     * @return bool
    */
    public function sortArrayInstalledModulesFirst($a, $b)
    {
        return strcmp($b['installed'], $a['installed']);
    }
}
