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

if (!defined('_PS_VERSION_')) {
    exit;
}

class ps_themecusto extends Module
{
    public $author_address;
    public $bootstrap;
    public $controller_name;
    public $front_controller = array();
    public $template_dir;
    public $js_path;
    public $css_path;
    public $img_path;
    public $logo_path;
    public $module_path;
    public $ready;

    public function __construct()
    {
        $this->name = 'ps_themecusto';
        $this->version = '1.0.9';
        $this->author = 'PrestaShop';
        $this->module_key = 'af0983815ad8c8a193b5dc9168e8372e';
        $this->author_address = '0x64aa3c1e4034d07015f639b0e171b0d7b27d01aa';
        $this->bootstrap = true;

        parent::__construct();
        $this->controller_name = array('AdminPsThemeCustoAdvanced', 'AdminPsThemeCustoConfiguration');
        if (!defined('PS_INSTALLATION_IN_PROGRESS')) {
            if (!$this->context instanceof Context) {
                throw new PrestaShopException("Undefined context");
            }
            $this->front_controller = array(
                $this->context->link->getAdminLink($this->controller_name[0]),
                $this->context->link->getAdminLink($this->controller_name[1]),
            );
        }
        $this->ps_versions_compliancy = array(
            'min' => '1.7',
            'max' => _PS_VERSION_
        );
        $this->displayName = $this->l('Theme Customization');
        $this->description = $this->l('Easily configure and customize your homepage’s theme and main native modules. Feature available on Design > Theme & Logo page.');
        $this->template_dir = '../../../../modules/'.$this->name.'/views/templates/admin/';
        $this->ps_uri = (Tools::usingSecureMode() ? Tools::getShopDomainSsl(true) : Tools::getShopDomain(true)).__PS_BASE_URI__;

        // Settings paths
        $this->js_path  = $this->_path.'views/js/';
        $this->css_path = $this->_path.'views/css/';
        $this->img_path = $this->_path.'views/img/';
        $this->logo_path = $this->_path.'logo.png';
        $this->module_path = $this->local_path;
        $this->ready = (getenv('PLATEFORM') === 'PSREADY')? true : false;
    }

    /**
     * install()
     *
     * @param none
     * @return bool
     */
    public function install()
    {
        if (parent::install() &&
            $this->installTabList()) {
            return true;
        } else {
            $this->_errors[] = $this->l('There was an error during the installation. Please contact us through Addons website');
            return false;
        }
    }

    /**
     * uninstall()
     *
     * @return bool
     */
    public function uninstall()
    {
        // unregister hook
        if (parent::uninstall() &&
            $this->uninstallTabList()) {
            return true;
        }

        $this->_errors[] = $this->l('There was an error during the uninstall. Please contact us through Addons website');
        return false;
    }

    /**
     * Assign all sub menu on Admin tab variable
     */
    public function assignTabList()
    {
        $themesTab = Tab::getInstanceFromClassName('AdminThemes');
        return array(
            array(
                'class'     => $this->controller_name[1],
                'active'    => true,
                'position'  => 2,
                'id_parent' => $themesTab->id_parent,
                'module'    => $this->name,
            ),
            array(
                'class'     => $this->controller_name[0],
                'active'    => true,
                'position'  => 3,
                'id_parent' => $themesTab->id_parent,
                'module'    => $this->name,
            )
        );
    }

    /**
     * Get all tab names by lang ISO
     */
    public function getTabNameByLangISO()
    {
        return array(
            $this->controller_name[1] => array(
                'fr'    => 'Configuration page d\'accueil',
                'en'    => 'Homepage Configuration',
                'es'    => 'Configuración página de inicio',
                'it'    => 'Configurazione homepage',
            ),
            $this->controller_name[0] => array(
                'fr'    => 'Personnalisation avancée',
                'en'    => 'Advanced Customization',
                'es'    => 'Personalización avanzada',
                'it'    => 'Personalizzazione avanzata',
            ),
        );
    }

    /**
     * Install all admin tab
     * @return boolean
     */
    public function installTabList()
    {
        /* First, we clone the tab "Theme & Logo" to redefined it correctly
            Without that, we can't have tabs in this section */
        $themesTab = Tab::getInstanceFromClassName('AdminThemes');
        $newTab = clone($themesTab);
        $newTab->id = 0;
        $newTab->id_parent = $themesTab->id_parent;
        $newTab->class_name = $themesTab->class_name.'Parent';
        $newTab->save();
        // Second save in order to get the proper position (add() resets it)
        $newTab->position = 0;
        $newTab->save();
        $themesTab->id_parent = $newTab->id;
        $themesTab->save();

        /* We install all the tabs from this module */
        $tab = new Tab();
        $aTabs = $this->assignTabList();
        $aTabsNameByLang = $this->getTabNameByLangISO();

        foreach ($aTabs as $aValue) {
            $tab->active = 1;
            $tab->class_name = $aValue['class'];
            $tab->name = array();

            foreach (Language::getLanguages(true) as $lang) {
                if (isset($aTabsNameByLang[$aValue['class']][$lang['iso_code']])) {
                    $sIsoCode = $lang['iso_code'];
                } else {
                    $sIsoCode = 'en';
                }
                $tab->name[$lang['id_lang']] =  $aTabsNameByLang[$aValue['class']][$sIsoCode];
            }

            $tab->id_parent = $aValue['id_parent'];
            $tab->module = $aValue['module'];
            $tab->position = $aValue['position'];
            $result = $tab->add();
            if (!$result) {
                return false;
            }
        }

        return ($result);
    }

    /**
     * uninstall tab
     *
     * @return bool
     */
    public function uninstallTabList()
    {
        $aTabs = $this->assignTabList();
        foreach ($aTabs as $aValue) {
            $id_tab = (int)Tab::getIdFromClassName($aValue['class']);
            if ($id_tab) {
                $tab = new Tab($id_tab);
                if (Validate::isLoadedObject($tab)) {
                    $result = $tab->delete();
                } else {
                    return false;
                }
            }
        }
        // Duplicate existing Theme tab for sub tree
        $themesTabParent = Tab::getInstanceFromClassName('AdminThemesParent');
        $themesTab = Tab::getInstanceFromClassName('AdminThemes');
        if (!$themesTabParent || !$themesTab) {
            return false;
        }
        $themesTab->id_parent = $themesTabParent->id_parent;
        $themesTabParent->delete();
        $themesTab->save();
        /* saving again for changing position to 0 */
        $themesTab->position = 0;
        $themesTab->save();
        return $result;
    }

    /**
     * set JS and CSS media
     */
    public function setMedia($aJsDef, $aJs, $aCss)
    {
        Media::addJsDef($aJsDef);

        array_push($aCss, $this->css_path."general.css");
        array_push($aJs, $this->js_path."general.js");
        $this->context->controller->addCSS($aCss);
        $this->context->controller->addJS($aJs);
    }

    /**
    * check if the employee has the right to use this admin controller
    * @return bool
    */
    public function hasEditRight()
    {
        $result = Profile::getProfileAccess(
            (int)Context::getContext()->cookie->profile,
            (int)Tab::getIdFromClassName($this->controller_name[0])
        );
        return (bool) $result['edit'];
    }

}
