<?php

namespace ICanBoogie;

/**
 * A formatted string.
 *
 * The string is formatted by replacing placeholders with the values provided.
 */
class FormattedString
{
	/**
	 * String format.
	 *
	 * @var string
	 */
	protected $format;

	/**
	 * An array of replacements for the placeholders.
	 *
	 * @var array
	 */
	protected $args;

	/**
	 * Initializes the {@link $format} and {@link $args} properties.
	 *
	 * @param string $format String format.
	 * @param array $args Format arguments.
	 *
	 * @see format()
	 */
	public function __construct($format, $args=null)
	{
		if (!is_array($args))
		{
			$args = func_get_args();
			array_shift($args);
		}

		$this->format = $format;
		$this->args = (array) $args;
	}

	/**
	 * Returns the string formatted with the {@link format()} function.
	 *
	 * @return string
	 */
	public function __toString()
	{
		return format($this->format, $this->args);
	}
}