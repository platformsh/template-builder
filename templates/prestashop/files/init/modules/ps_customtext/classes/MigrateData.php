<?php
/*
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
 *  @author PrestaShop SA <contact@prestashop.com>
 *  @copyright  2007-2018 PrestaShop SA
 *  @license    http://opensource.org/licenses/osl-3.0.php  Open Software License (OSL 3.0)
 *  International Registered Trademark & Property of PrestaShop SA
 */

/**
 * Database may change between two version of the module, or between the 1.6 and 1.7 modules.
 * This class allow the data to be kept during upgrades and migrations.
 */
class MigrateData
{
    private $loadedData = array();

    /**
     * This methods retrieves data from older database models
     * - ps_customtext < v3.0.0
     * - blockcmsinfo (1.6 equivalent module)
     *
     * @return array
     */
    public function retrieveOldData()
    {
        $this->loadedData = array();
        $texts = Db::getInstance()->executeS('SELECT i.`id_shop`, il.`id_lang`, il.`text` FROM `' . _DB_PREFIX_ . 'info` i
            INNER JOIN `' . _DB_PREFIX_ . 'info_lang` il ON il.`id_info` = i.`id_info`'
        );

        if (is_array($texts) && !empty($texts)) {
            foreach ($texts as $text) {
                $this->loadedData[(int)$text['id_shop']][(int)$text['id_lang']] = $text['text'];
            }
        }

        return $this->loadedData;
    }

    /**
     * Import the old CustomText data in the new structure
     *
     * @return bool
     */
    public function insertData()
    {
        if (empty($this->loadedData)) {
            return true;
        }
        
        $return = true;
        $shopsIds = Shop::getShops(true, null, true);
        $customTexts = array_intersect_key($this->loadedData, $shopsIds);

        $info = new CustomText();
        $info->text = reset($customTexts);
        $return &= $info->add();

        if (sizeof($customTexts) > 1) {
            foreach ($customTexts as $key => $text) {
                Shop::setContext(Shop::CONTEXT_SHOP, (int) $key);
                $info->text = $text;
                $return &= $info->save();
            }
        }

        return $return;
    }
}
