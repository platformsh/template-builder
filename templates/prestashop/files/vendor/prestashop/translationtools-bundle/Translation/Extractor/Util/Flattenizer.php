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

namespace PrestaShop\TranslationToolsBundle\Translation\Extractor\Util;

use Symfony\Component\Filesystem\Filesystem;
use Symfony\Component\Finder\Finder;

/**
 * This class have only one thing to do, transform:
 *
 * en-US
 *   ├── Admin
 *   │   └── Catalog
 *   │        ├── Feature.xlf
 *   │        ├── Help.xlf
 *   │        └── Notification.xlf
 *   └── Shop
 *        └── PDF.xlf
 *
 *
 * Into:
 *
 * ├── AdminCatalogFeature.en-US.xlf
 * ├── AdminCatalogHelp.en-US.xlf
 * ├── AdminCatalogNotification.en-US.xlf
 * └── ShopPDF.en-US.xlf
 */
class Flattenizer
{
    public static $finder = null;

    public static $filesystem = null;

    /**
     * @input string $inputPath Path of directory to flattenize
     * @input string $outputPath Location of flattenized files newly created
     * @input string $locale Selected locale for theses files.
     * @input boolean $cleanPath Clean input path after flatten.
     */
    public static function flatten($inputPath, $outputPath, $locale, $cleanPath = true)
    {
        $finder = self::$finder;
        $filesystem = self::$filesystem;

        if (is_null(self::$finder)) {
            $finder = new Finder();
        }

        if (is_null(self::$filesystem)) {
            $filesystem = new Filesystem();
        }

        if ($cleanPath) {
            $filesystem->remove($outputPath);
            $filesystem->mkdir($outputPath);
        }

        return self::flattenFiles($finder->in($inputPath)->files(), $outputPath, $locale, $filesystem);
    }

    /**
     * @param SplFileInfo $files List of files to flattenize
     * @param string $outputPath Location of flattenized files newly created
     * @param string $locale Selected locale for theses files
     * @param Filesystem $filesystem Instance of Filesystem
     * @param bool $addLocale Should add the locale to filename
     * @return bool
     */
    public static function flattenFiles($files, $outputPath, $locale, $filesystem, $addLocale = true)
    {
        foreach ($files as $file) {
            $flatName = preg_replace('#[\/\\\]#', '', $file->getRelativePath()).$file->getFilename();

            if ($addLocale) {
                $flatName = preg_replace('#\.xlf#', '.'.$locale.'.xlf', $flatName);
            }

            $filesystem->copy($file->getRealpath(), $outputPath.'/'.$flatName);
        }
        return true;
    }
}
