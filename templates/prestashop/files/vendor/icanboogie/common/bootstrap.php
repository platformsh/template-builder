<?php

/*
 * This file is part of the ICanBoogie package.
 *
 * (c) Olivier Laviale <olivier.laviale@gmail.com>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace ICanBoogie;

/**
 * The charset used by the application. Defaults to "utf-8".
 *
 * @var string
 */
defined('ICanBoogie\CHARSET') or define('ICanBoogie\CHARSET', 'utf-8');

if (function_exists('mb_internal_encoding'))
{
	mb_internal_encoding(CHARSET);
}