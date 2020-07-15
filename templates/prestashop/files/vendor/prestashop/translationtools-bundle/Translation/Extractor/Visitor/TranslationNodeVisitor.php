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

namespace PrestaShop\TranslationToolsBundle\Translation\Extractor\Visitor;

use PhpParser\NodeVisitorAbstract;
use PhpParser\Node;
use PhpParser\Node\Expr\MethodCall;
use PhpParser\Node\Expr\FuncCall;
use PhpParser\Node\Scalar\String_;
use PhpParser\Node\Arg;

class TranslationNodeVisitor extends NodeVisitorAbstract
{
    protected $file;

    /**
     * @var array
     */
    protected $supportMethods = ['l', 'trans', 't'];

    /**
     * @var array
     */
    protected $translations = [];

    /**
     * @var array
     */
    protected $comments = [];

    /**
     * TranslationNodeVisitor constructor.
     *
     * @param $file
     */
    public function __construct($file)
    {
        $this->file = $file;
    }

    /**
     * {@inheritdoc}
     */
    public function leaveNode(Node $node)
    {
        $comments = $node->getAttribute('comments');

        if (is_array($comments)) {
            foreach ($comments as $comment) {
                $this->comments[] = [
                    'line' => $comment->getLine(),
                    'file' => $this->file,
                    'comment' => trim($comment->getText(), " \t\n\r\0\x0B/*"),
                ];
            }
        }

        if ($node instanceof MethodCall || $node instanceof FuncCall) {
            if ((!is_string($node->name) && !is_a($node->name, 'PhpParser\Node\Name')) || empty($node->args)) {
                return;
            } elseif (is_a($node->name, 'PhpParser\Node\Name')) {
                $nodeName = $node->name->parts[0];
            } else {
                $nodeName = $node->name;
            }

            $key = $this->getValue($node->args[0]);
            if (in_array($nodeName, $this->supportMethods) && !empty($key)) {
                $translation = [
                    'source' => $key,
                    'line' => $node->args[0]->getLine(),
                ];

                if ($nodeName == 'trans' && count($node->args) > 2 && $node->args[2]->value instanceof String_) {
                    $translation['domain'] = $node->args[2]->value->value;
                } elseif ($nodeName == 't') {
                    $translation['domain'] = 'Emails.Body';
                }

                $this->translations[] = $translation;
            }
        }
    }

    /**
     * @param Arg $arg
     *
     * @return string|null
     */
    protected function getValue(Arg $arg)
    {
        if ($arg->value instanceof String_) {
            return $arg->value->value;
        } elseif (gettype($arg) === 'string') {
            return $arg->value;
        }
    }

    /**
     * @return array
     */
    public function getTranslations()
    {
        return $this->translations;
    }

    /**
     * @return array
     */
    public function getComments()
    {
        return $this->comments;
    }
}
