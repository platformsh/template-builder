<?php

namespace PrestaShop\TranslationToolsBundle\Twig\NodeVisitor;

use Symfony\Bridge\Twig\NodeVisitor\TranslationNodeVisitor as BaseTranslationNodeVisitor;
use Symfony\Bridge\Twig\Node\TransNode;

class TranslationNodeVisitor extends BaseTranslationNodeVisitor
{
    const UNDEFINED_DOMAIN = '_undefined';

    private $enabled = true;
    private $messages = array();

    public function enable()
    {
        $this->enabled = true;
        $this->messages = array();
    }

    public function getMessages()
    {
        return $this->messages;
    }

    /**
     * {@inheritdoc}
     */
    protected function doEnterNode(\Twig_Node $node, \Twig_Environment $env)
    {
        if (!$this->enabled) {
            return $node;
        }

        if (
            $node instanceof \Twig_Node_Expression_Filter &&
            'trans' === $node->getNode('filter')->getAttribute('value') &&
            $node->getNode('node') instanceof \Twig_Node_Expression_Constant
        ) {
            // extract constant nodes with a trans filter
            $this->messages[] = array(
                $node->getNode('node')->getAttribute('value'),
                $this->getReadDomainFromArguments($node->getNode('arguments'), 1),
                'line' => $node->getTemplateLine(),
            );
        } elseif (
            $node instanceof \Twig_Node_Expression_Filter &&
            'transchoice' === $node->getNode('filter')->getAttribute('value') &&
            $node->getNode('node') instanceof \Twig_Node_Expression_Constant
        ) {
            // extract constant nodes with a trans filter
            $this->messages[] = array(
                $node->getNode('node')->getAttribute('value'),
                $this->getReadDomainFromArguments($node->getNode('arguments'), 2),
                'line' => $node->getTemplateLine(),
            );
        } elseif ($node instanceof TransNode) {
            // extract trans nodes
            $this->messages[] = array(
                $node->getNode('body')->getAttribute('data'),
                $this->getReadDomainFromNode($node->getNode('domain')),
                'line' => $node->getTemplateLine(),
            );
        }

        return $node;
    }

    /**
     * @param \Twig_Node $arguments
     * @param int        $index
     *
     * @return string|null
     */
    private function getReadDomainFromArguments(\Twig_Node $arguments, $index)
    {
        if ($arguments->hasNode('domain')) {
            $argument = $arguments->getNode('domain');
        } elseif ($arguments->hasNode($index)) {
            $argument = $arguments->getNode($index);
        } else {
            return;
        }

        return $this->getReadDomainFromNode($argument);
    }

    /**
     * @param \Twig_Node $node
     *
     * @return string|null
     */
    private function getReadDomainFromNode(\Twig_Node $node = null)
    {
        if (null === $node) {
            return;
        }

        if ($node instanceof \Twig_Node_Expression_Constant) {
            return $node->getAttribute('value');
        }

        return self::UNDEFINED_DOMAIN;
    }
}
