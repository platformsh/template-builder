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

use PrestaShop\TranslationToolsBundle\Twig\Lexer;
use Symfony\Bridge\Twig\Translation\TwigExtractor as BaseTwigExtractor;
use Symfony\Component\Finder\SplFileInfo;
use Symfony\Component\Translation\MessageCatalogue;
use Symfony\Component\Translation\Extractor\ExtractorInterface;

class TwigExtractor extends BaseTwigExtractor implements ExtractorInterface
{
    use TraitExtractor;

    /**
     * Prefix for found message.
     *
     * @var string
     */
    private $prefix = '';

    /**
     * The twig environment.
     *
     * @var \Twig_Environment
     */
    private $twig;

    /**
     * @var \Twig_Lexer
     */
    private $twigLexer;

    /**
     * The twig environment.
     *
     * @var \Twig_Environment
     */
    public function __construct(\Twig_Environment $twig)
    {
        $this->twig = $twig;
        $this->twigLexer = new \Twig_Lexer($this->twig);
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

            try {
                $this->extractTemplateFile($file, $catalogue);
            } catch (\Twig_Error $e) {
                if ($file instanceof SplFileInfo) {
                    $e->setSourceContext(new \Twig_Source(
                        $e->getSourceContext()->getCode(),
                        $e->getSourceContext()->getName(),
                        $file->getRelativePathname()
                    ));
                } elseif ($file instanceof \SplFileInfo) {
                    $e->setSourceContext(new \Twig_Source(
                        $e->getSourceContext()->getCode(),
                        $e->getSourceContext()->getName(),
                        $file->getRealPath()
                    ));
                }

                throw $e;
            }
        }
    }

    /**
     * {@inheritdoc}
     */
    protected function extractTemplateFile($file, MessageCatalogue $catalogue)
    {
        if (!$file instanceof \SplFileInfo) {
            $file = new \SplFileInfo($file);
        }

        $visitor = $this->twig->getExtension('translator')->getTranslationNodeVisitor();
        $visitor->enable();

        $this->twig->setLexer(new Lexer($this->twig));

        $tokens = $this->twig->tokenize(file_get_contents($file->getPathname()), $file->getFilename());
        $this->twig->parse($tokens);

        $comments = $this->twigLexer->getComments();

        foreach ($visitor->getMessages() as $message) {
            $domain = $this->resolveDomain(isset($message[1]) ? $message[1] : null);

            $catalogue->set(
                $message[0],
                $this->prefix.trim($message[0]),
                $domain
            );

            $metadata = [
                'file' => $file->getRealpath(),
                'line' => $message['line'],
            ];

            $comment = $this->getEntryComment($comments, $file->getFilename(), ($message['line'] - 1));

            if (null != $comment) {
                $metadata['comment'] = $comment;
            }

            if (isset($message['line'])) {
                $metadata['comment'] = $this->getEntryComment($comments, $file->getFilename(), ($message['line'] - 1));
            }

            $catalogue->setMetadata($message[0], $metadata, $domain);
        }

        $visitor->disable();
    }

    /**
     * @param $comments
     * @param $file
     * @param $line
     *
     * @return array
     */
    public function getEntryComment($comments, $file, $line)
    {
        foreach ($comments as $comment) {
            if ($comment['file'] == $file && $comment['line'] == $line) {
                return $comment['comment'];
            }
        }
    }

    /**
     * @param string $directory
     *
     * @return Finder
     */
    protected function extractFromDirectory($directory)
    {
        return $this->getFinder()->files()->name('*.twig')->in($directory);
    }
}
