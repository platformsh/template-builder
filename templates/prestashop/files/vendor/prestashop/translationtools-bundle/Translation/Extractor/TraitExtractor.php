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

use Symfony\Component\Finder\Finder;

trait TraitExtractor
{
    protected $defaultDomain = 'messages';

    /**
     * @var Finder
     */
    protected $finder;

    /**
     * @param $domainName
     *
     * @return string
     */
    protected function resolveDomain($domainName)
    {
        if (empty($domainName)) {
            return $this->defaultDomain;
        }

        return $domainName;
    }

    /**
     * @param $comments
     * @param $file
     * @param $line
     *
     * @return array
     */
    public function getEntryComment(array $comments, $file, $line)
    {
        foreach ($comments as $comment) {
            if ($comment['file'] == $file && $comment['line'] == $line) {
                return $comment['comment'];
            }
        }
    }

    /**
     * @param $finder
     *
     * @return $this
     */
    public function setFinder(Finder $finder)
    {
        $this->finder = $finder;

        return $this;
    }

    /**
     * @return Finder
     */
    public function getFinder()
    {
        if (null === $this->finder) {
            return new Finder();
        }

        return $this->finder;
    }
}
