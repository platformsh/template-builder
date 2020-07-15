<?php

/**
 * 2007-2016 PrestaShop.
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
 * @author    PrestaShop SA <contact@prestashop.com>
 * @copyright 2007-2015 PrestaShop SA
 * @license   http://opensource.org/licenses/osl-3.0.php Open Software License (OSL 3.0)
 * International Registered Trademark & Property of PrestaShop SA
 */

namespace PrestaShop\TranslationToolsBundle\Translation;

class MultilanguageCatalog
{
    /** @var [] $messages (key/locale) */
    private $messages = [];

    /**
     * @param string|int $key
     * @param string|int $locale
     *
     * @return bool
     */
    public function has($key, $locale = null)
    {
        return !empty($this->messages[$key]) && (is_null($locale) || !empty($this->messages[$key][$locale]));
    }

    /**
     * @param string|int $key
     * @param string|int $locale
     *
     * @return mixed
     */
    public function get($key, $locale = null)
    {
        if (is_null($locale)) {
            return $this->messages[$key];
        }

        return $this->messages[$key][$locale];
    }

    /**
     * @param string|int $key
     * @param string|int $locale
     * @param mixed      $translation
     */
    public function set($key, $locale, $translation)
    {
        if (!isset($this->messages[$key])) {
            $this->messages[$key] = [];
        }

        $this->messages[$key][$locale] = $translation;

        return $this;
    }
}
