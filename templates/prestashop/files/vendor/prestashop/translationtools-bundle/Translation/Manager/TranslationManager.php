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

namespace PrestaShop\TranslationToolsBundle\Translation\Manager;

use PrestaShop\TranslationToolsBundle\Translation\Parser\CrowdinPhpParser;
use PrestaShop\TranslationToolsBundle\Translation\MultilanguageCatalog;
use Symfony\Component\Finder\Finder;

class TranslationManager
{
    /** @var MultilanguageCatalog $catalogue */
    private $catalog;

    /** @var CrowdinPhpParser $parser */
    private $parser;

    /**
     * @param CrowdinPhpParser $crodwinPhpParser
     */
    public function __construct(CrowdinPhpParser $crodwinPhpParser)
    {
        $this->parser = $crodwinPhpParser;
        $this->catalog = new MultilanguageCatalog();
    }

    /**
     * @param string $filePath
     * @param string $key
     *
     * @return string
     */
    public function get($filePath, $key)
    {
        if (!$this->catalog->has($key)) {
            $this->extractFile($filePath);
        }

        return $this->catalog->has($key) ? $this->catalog->get($key) : null;
    }

    /**
     * @param string $filePath
     */
    private function extractFile($filePath)
    {
        $finder = new Finder();

        $fullpath = preg_replace('/([a-z]{2}-[A-Z]{2})/', '*', $filePath);
        $filename = basename($fullpath);
        $directory = pathinfo(str_replace('*', '', $fullpath), PATHINFO_DIRNAME);

        if (!file_exists($directory)) {
            return false;
        }

        $files = $finder->files()->name($filename)->in($directory);

        foreach ($files as $file) {
            if (preg_match('/([a-z]{2}-[A-Z]{2})/', $file->getRealpath(), $matches)) {
                $generator = $this->parser->parseFileTokens($file->getRealpath());

                for (; $generator->valid(); $generator->next()) {
                    $translation = $generator->current();

                    if (!empty($translation['message'])) {
                        $this->catalog->set($translation['key'], $matches[1], $translation['message']);
                    }
                }
            }
        }
    }
}
