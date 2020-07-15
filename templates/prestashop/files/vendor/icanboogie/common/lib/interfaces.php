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

interface ToArray
{
	/**
	 * Converts the object into an array.
	 *
	 * @return array
	 */
	public function to_array();
}

interface ToArrayRecursive extends ToArray
{
	/**
	 * Converts the object into an array recursively.
	 *
	 * @return array
	 */
	public function to_array_recursive();
}