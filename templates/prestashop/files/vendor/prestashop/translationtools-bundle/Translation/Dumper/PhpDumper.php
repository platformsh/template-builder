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

namespace PrestaShop\TranslationToolsBundle\Translation\Dumper;

use PrestaShop\TranslationToolsBundle\Translation\Builder\PhpBuilder;
use PrestaShop\TranslationToolsBundle\Translation\Helper\LegacyHelper;
use Symfony\Component\Translation\Dumper\FileDumper;
use Symfony\Component\Translation\MessageCatalogue;
use Symfony\Component\Filesystem\Filesystem;

class PhpDumper extends FileDumper
{
    /**
     * @var PhpBuilder[]
     */
    private $builders = [];

    /**
     * {@inheritdoc}
     */
    public function dump(MessageCatalogue $messages, $options = array())
    {
        if (!array_key_exists('path', $options)) {
            throw new \InvalidArgumentException('The file dumper needs a path option.');
        }

        if (array_key_exists('default_locale', $options)) {
            $defaultLocale = $options['default_locale'];
        } else {
            $defaultLocale = $messages->getLocale();
        }

        // Add/update all Php builders (1/file)
        foreach ($messages->getDomains() as $domain) {
            $this->formatCatalogue($messages, $domain);
        }

        // Create files
        foreach ($this->builders as $filename => $builder) {
            $fullpath = $options['path'].'/'.$filename;
            $directory = dirname($fullpath);

            if (!file_exists($directory) && !@mkdir($directory, 0777, true)) {
                throw new \RuntimeException(sprintf('Unable to create directory "%s".', $directory));
            }

            $fs = new Filesystem();
            $fs->dumpFile($fullpath, $builder->build());
        }
    }

    /**
     * {@inheritdoc}
     */
    public function formatCatalogue(MessageCatalogue $messages, $domain, array $options = array())
    {
        foreach ($messages->all($domain) as $source => $target) {
            $metadata = $messages->getMetadata($source, $domain);

            // Skip if output info can't be guessed
            if (!($outputInfo = LegacyHelper::getOutputInfo($metadata['file']))) {
                continue;
            }

            $outputFile = str_replace('[locale]', $messages->getLocale(), $outputInfo['file']);

            if (!isset($this->builders[$outputFile])) {
                $this->builders[$outputFile] = new PhpBuilder();
                $this->builders[$outputFile]->appendGlobalDeclaration($outputInfo['var']);
            }

            $this->builders[$outputFile]->appendStringLine(
                $outputInfo['var'],
                $outputInfo['generateKey']($target),
                $target
            );
        }
    }

    /**
     * {@inheritdoc}
     */
    public function getExtension()
    {
        return 'php';
    }
}
