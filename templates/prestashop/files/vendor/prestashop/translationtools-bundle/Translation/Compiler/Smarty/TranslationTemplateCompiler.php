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

namespace PrestaShop\TranslationToolsBundle\Translation\Compiler\Smarty;

use SmartyException;
use SmartyCompilerException;
use Smarty_Internal_SmartyTemplateCompiler;
use Smarty_Internal_Templateparser;
use Smarty_Internal_Template;
use Symfony\Component\Filesystem\Exception\FileNotFoundException;

class TranslationTemplateCompiler extends Smarty_Internal_SmartyTemplateCompiler
{
    /**
     *  Inherited from Smarty_Internal_TemplateCompilerBase.
     *
     * @var Smarty_Internal_Template
     * @var bool                     $inheritance_child
     *
     * Inherited from Smarty_Internal_SmartyTemplateCompiler
     * @var Smarty $smarty
     * @var string $lexer_class
     * @var object $lex
     * @var string $parser_class
     * @var object $parser
     */

    /**
     * @var bool
     */
    public $nocache = false;

    /**
     * @var bool
     */
    public $tag_nocache = false;

    /**
     * @var bool
     */
    private $abort_and_recompile = false;

    /**
     * @var string
     */
    private $templateFile;

    /**
     * @return array
     */
    public function getTranslationTags()
    {
        $this->init();
        $tagFound = [];
        $comment = [];

        // get tokens from lexer and parse them
        while ($this->lex->yylex() && !$this->abort_and_recompile) {
            try {
                if ('extends' == $this->lex->value) {
                    $this->lex->value = 'dummy';
                }

                $this->parser->doParse($this->lex->token, $this->lex->value);
                if ($this->lex->token === Smarty_Internal_Templateparser::TP_TEXT) {
                    $comment = [
                        'line' => $this->lex->line,
                        'value' => $this->lex->value,
                    ];
                }
            } catch (SmartyCompilerException $e) {
                if (($tag = $this->explodeLTag($this->parser->yystack))) {
                    $tagFound[] = $this->getTag($tag, $e, $comment);
                }

                $this->parser->yy_accept();
            } catch (SmartyException $e) {
            }
        }

        return $tagFound;
    }

    /**
     * @param string $templateFile
     */
    public function setTemplateFile($templateFile)
    {
        if (!file_exists($templateFile)) {
            throw new FileNotFoundException(null, 0, null, $templateFile);
        }

        $this->templateFile = $templateFile;

        return $this;
    }

    private function init()
    {
        /* here is where the compiling takes place. Smarty
          tags in the templates are replaces with PHP code,
          then written to compiled files. */
        // init the lexer/parser to compile the template
        $this->parent_compiler = $this;
        $this->template = new Smarty_Internal_Template($this->templateFile, $this->smarty);
        $this->lex = new $this->lexer_class(file_get_contents($this->templateFile), $this);
        $this->parser = new $this->parser_class($this->lex, $this);

        if (((int) ini_get('mbstring.func_overload')) & 2) {
            mb_internal_encoding('ASCII');
        }
    }

    /**
     * @param string   $string
     * @param null|int $token
     *
     * @return string
     */
    private function naturalize($string, $token = null)
    {
        switch ($token) {
            case Smarty_Internal_Templateparser::TP_TEXT:
                return trim($string, " \t\n\r\0\x0B{*}");
            default:
                return substr($string, 1, -1);
        }
    }

    /**
     * @param array $tagStack
     *
     * @return array|null
     */
    private function explodeLTag(array $tagStack)
    {
        $tag = null;

        foreach ($tagStack as $entry) {
            if ($entry->minor === 'l') {
                $tag = [];
            }

            if (is_array($tag) && is_array($entry->minor)) {
                foreach ($entry->minor as $minor) {
                    foreach ($minor as $attr => $val) {
                        // Skip on variables
                        if (0 === strpos($val, '$') && 's' === $attr) {
                            return;
                        }

                        $tag[$attr] = $this->naturalize($val);
                    }
                }
            }
        }

        return $tag;
    }

    /**
     * @param array                   $value
     * @param SmartyCompilerException $exception
     * @param array                   $previousComment
     *
     * @return array
     */
    private function getTag(array $value, SmartyCompilerException $exception, array $previousComment)
    {
        $tag = [
            'tag' => $value,
            'line' => $exception->line,
            'template' => $exception->template,
        ];

        if (!empty($previousComment) && $previousComment['line'] == $tag['line'] - 1) {
            $tag['comment'] = $this->naturalize($previousComment['value'], Smarty_Internal_Templateparser::TP_TEXT);
        }

        return $tag;
    }
}
