<?php

namespace PrestaShop\TranslationToolsBundle;

use Smarty as BaseSmarty;

class Smarty extends BaseSmarty
{
    public function forceCompile($value)
    {
        return $this->force_compile = $value;
    }
}
