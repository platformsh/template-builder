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

namespace PrestaShop\TranslationToolsBundle;

use Symfony\Component\OptionsResolver\OptionsResolver;
use Symfony\Component\Yaml\Yaml;

class Configuration
{
    /**
     * @var array
     */
    private static $paths = [];

    /**
     * @var array
     */
    private static $excludeFiles = [];

    /**
     * @var string
     */
    private static $projectDirectory = '';

    /**
     * @var string
     */
    private static $cacheDir;

    /**
     * @param array $arr
     */
    public static function fromArray(array $arr)
    {
        $optionsResolver = new OptionsResolver();
        $options = $optionsResolver->setRequired([
            'paths',
            'exclude_files',
        ])
            ->setDefaults([
                'cache_dir' => null,
            ])
            ->addAllowedTypes('paths', 'array')
            ->addAllowedTypes('exclude_files', ['array', 'null'])
            ->addAllowedTypes('cache_dir', ['string', 'null'])
            ->resolve($arr);

        self::$paths = (array) $options['paths'];
        self::$excludeFiles = (array) $options['exclude_files'];
        self::$cacheDir = $options['cache_dir'];
    }

    /**
     * @param string $yamlFile
     */
    public static function fromYamlFile($yamlFile)
    {
        self::$projectDirectory = realpath(dirname($yamlFile));
        self::fromArray(Yaml::parse(file_get_contents($yamlFile)));
    }

    /**
     * @return array
     */
    public static function getPaths()
    {
        return self::$paths;
    }

    /**
     * @return array
     */
    public static function getExcludeFiles()
    {
        return self::$excludeFiles;
    }

    /**
     * @return string
     */
    public static function getProjectDirectory()
    {
        return self::$projectDirectory;
    }

    /**
     * @param string $path
     * @param string|bool $rootDir
     *
     * @return string
     */
    public static function getRelativePath($path, $rootDir = false)
    {
        $realpath = realpath($path);
        $path = empty($realpath) ? $path : $realpath;

        if (!empty($rootDir)) {
            $rootDir = rtrim($rootDir, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;
        } else {
            $rootDir = '';
        }

        return str_replace($rootDir, '', $path);
    }

    /**
     * @return string
     */
    public static function getCacheDir()
    {
        return empty(self::$cacheDir) ? sys_get_temp_dir().DIRECTORY_SEPARATOR : self::$cacheDir;
    }
}
