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

use Symfony\Component\Translation\Extractor\ChainExtractor as BaseChaineExtractor;
use Symfony\Component\Translation\MessageCatalogue;
use Symfony\Component\Finder\Finder;
use Symfony\Component\Translation\Extractor\ExtractorInterface;
use PrestaShop\TranslationToolsBundle\Configuration;

class ChainExtractor extends BaseChaineExtractor
{
    /**
     * The extractors.
     *
     * @var ExtractorInterface[]
     */
    private $extractors = [];

    /**
     * @param string             $format
     * @param ExtractorInterface $extractor
     *
     * @return self
     */
    public function addExtractor($format, ExtractorInterface $extractor)
    {
        $this->extractors[$format] = $extractor;

        return $this;
    }

    /**
     * {@inheritdoc}
     */
    public function extract($directory, MessageCatalogue $catalogue)
    {
        $finder = new Finder();

        $finder->ignoreUnreadableDirs();

        foreach (Configuration::getPaths() as $item) {
            $finder->path('{^'.$item.'}');
        }

        foreach (Configuration::getExcludeFiles() as $item) {
            $finder->notPath('{^'.$item.'}');
        }

        foreach ($this->extractors as $extractor) {
            $extractor->setFinder(clone $finder);
            $extractor->extract($directory, $catalogue);
        }
    }
}
