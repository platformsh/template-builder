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

trait ToArrayRecursiveTrait
{
	public function to_array_recursive()
	{
		$array = $this->to_array();

		foreach ($array as $key => &$value)
		{
			if ($value instanceof ToArrayRecursive)
			{
				$value = $value->to_array_recursive();
			}
			else if ($value instanceof ToArray)
			{
				$value = $value->to_array();
			}
		}

		return $array;
	}
}