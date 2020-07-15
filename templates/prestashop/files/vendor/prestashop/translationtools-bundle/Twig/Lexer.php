<?php

namespace PrestaShop\TranslationToolsBundle\Twig;

class Lexer extends \Twig_Lexer
{
    /**
     * @var array
     */
    protected $comments = [];

    /**
     * @var bool
     */
    protected $call = false;

    protected function lexComment()
    {
        parent::lexComment();

        if (true === $this->call) {
            return;
        }

        preg_match_all('|\{#\s(.+)\s#\}|i', $this->code, $commentMatch);

        if (is_array($commentMatch[1])) {
            foreach ($commentMatch[1] as $comment) {
                $this->comments[] = array(
                    'line' => $this->lineno,
                    'comment' => $comment,
                    'file' => $this->filename,
                );
            }
        }

        $this->call = true;
    }

    public function getComments()
    {
        return $this->comments;
    }
}
