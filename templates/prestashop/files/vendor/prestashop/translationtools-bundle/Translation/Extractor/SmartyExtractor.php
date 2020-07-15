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

namespace PrestaShop\TranslationToolsBundle\Translation\Extractor;

use SplFileInfo;
use PrestaShop\TranslationToolsBundle\Translation\Compiler\Smarty\TranslationTemplateCompiler;
use Symfony\Component\Translation\Extractor\AbstractFileExtractor;
use Symfony\Component\Translation\Extractor\ExtractorInterface;
use Symfony\Component\Translation\MessageCatalogue;

class SmartyExtractor extends AbstractFileExtractor implements ExtractorInterface
{
    use TraitExtractor;

    /**
     * @var TranslationTemplateCompiler
     */
    private $smartyCompiler;
    private $prefix;

    /**
     * @param TranslationTemplateCompiler $smartyCompiler
     */
    public function __construct(TranslationTemplateCompiler $smartyCompiler)
    {
        $this->smartyCompiler = $smartyCompiler;
    }

    /**
     * {@inheritdoc}
     */
    public function extract($resource, MessageCatalogue $catalogue)
    {
        $files = $this->extractFiles($resource);
        foreach ($files as $file) {
            if (!$this->canBeExtracted($file->getRealpath())) {
                continue;
            }

            $this->extractFromFile($file, $catalogue);
        }
    }

    /**
     * @param SplFileInfo      $resource
     * @param MessageCatalogue $catalogue
     */
    protected function extractFromFile(SplFileInfo $resource, MessageCatalogue $catalogue)
    {
        foreach ($this->smartyCompiler->setTemplateFile($resource->getPathname())->getTranslationTags() as $translation) {
            $domain = $this->resolveDomain(isset($translation['tag']['d']) ? $translation['tag']['d'] : null);
            $string = stripslashes($translation['tag']['s']);

            $catalogue->set($this->prefix.$string, $string, $domain);
            $catalogue->setMetadata(
                $this->prefix.$string,
                [
                    'line' => $translation['line'],
                    'file' => $translation['template'],
                ],
                $domain
            );
        }
    }

    /**
     * {@inheritdoc}
     */
    public function setPrefix($prefix)
    {
        $this->prefix = $prefix;
    }

    /**
     * {@inheritdoc}
     */
    protected function canBeExtracted($file)
    {
        return $this->isFile($file) && 'tpl' === pathinfo($file, PATHINFO_EXTENSION);
    }

    /**
     * {@inheritdoc}
     */
    protected function extractFromDirectory($directory)
    {
        return $this->getFinder()->name('*.tpl')->in($directory);
    }
}
