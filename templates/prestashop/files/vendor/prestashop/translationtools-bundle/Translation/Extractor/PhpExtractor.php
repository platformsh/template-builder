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

use Symfony\Component\Translation\Extractor\AbstractFileExtractor;
use Symfony\Component\Translation\Extractor\ExtractorInterface;
use Symfony\Component\Translation\MessageCatalogue;
use PhpParser\ParserFactory;
use PhpParser\Lexer;
use PhpParser\NodeTraverser;
use PrestaShop\TranslationToolsBundle\Translation\Extractor\Visitor\TranslationNodeVisitor;

class PhpExtractor extends AbstractFileExtractor implements ExtractorInterface
{
    use TraitExtractor;

    /**
     * @var array
     */
    protected $visitors = [];

    /**
     * Prefix for new found message.
     *
     * @var string
     */
    private $prefix = '';

    /**
     * @var \PhpParser\Parser\Multiple
     */
    private $parser;

    public function __construct()
    {
        $lexer = new Lexer(array(
            'usedAttributes' => array(
                'comments', 'startLine', 'endLine', 'startTokenPos', 'endTokenPos',
            ),
        ));

        $this->parser = (new ParserFactory())->create(ParserFactory::PREFER_PHP7, $lexer);
    }

    /**
     * {@inheritdoc}
     */
    public function extract($resource, MessageCatalogue $catalogue)
    {
        $files = $this->extractFiles($resource);

        foreach ($files as $file) {
            $this->parseFileTokens($file, $catalogue);
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
     * @param $file
     * @param MessageCatalogue $catalog
     *
     * @throws \Exception
     */
    protected function parseFileTokens($file, MessageCatalogue $catalog)
    {
        $code = file_get_contents($file);

        $nodeVisitor = new TranslationNodeVisitor($file->getFilename());
        $traverser = new NodeTraverser();
        $traverser->addVisitor($nodeVisitor);

        try {
            $stmts = $this->parser->parse($code);
            $traverser->traverse($stmts);

            $comments = $nodeVisitor->getComments();

            foreach ($nodeVisitor->getTranslations() as $translation) {
                $translation['domain'] = empty($translation['domain']) ? $this->resolveDomain(null) :  $translation['domain'];
                $comment = $metadata['comment'] = $this->getEntryComment($comments, $file->getFilename(), ($translation['line'] - 1));

                $catalog->set($translation['source'], $this->prefix.trim($translation['source']), $translation['domain']);
                $catalog->setMetadata(
                    $translation['source'],
                    [
                        'line' => $translation['line'],
                        'file' => $file->getRealPath(),
                        'comment' => $comment,
                    ],
                    $translation['domain']
                );
            }
        } catch (\PhpParser\Error $e) {
            throw new \Exception(
                sprintf('Could not parse tokens in "%s" file. Is it syntactically valid?', $file),
                $e->getCode(),
                $e
            );
        }
    }

    /**
     * @param string $file
     *
     * @throws \InvalidArgumentException
     *
     * @return bool
     */
    protected function canBeExtracted($file)
    {
        return $this->isFile($file) && 'php' === pathinfo($file, PATHINFO_EXTENSION);
    }

    /**
     * @param string|array $directory
     *
     * @return array
     */
    protected function extractFromDirectory($directory)
    {
        return $this->getFinder()->files()->name('*.php')->in($directory);
    }
}
