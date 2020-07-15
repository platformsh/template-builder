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
 * Exception thrown when there is something wrong with an array offset.
 *
 * This is the base class for offset exceptions, one should rather use the
 * {@link OffsetNotReadable} or {@link OffsetNotWritable} exceptions.
 */
class OffsetError extends \RuntimeException
{

}

/**
 * Exception thrown when an array offset is not defined.
 *
 * For example, this could be triggered by an offset out of bounds while setting an array value.
 */
class OffsetNotDefined extends OffsetError
{
	public function __construct($message, $code=500, \Exception $previous=null)
	{
		if (is_array($message))
		{
			list($offset, $container) = $message + array(1 => null);

			if (is_object($container))
			{
				$message = format
				(
					'Undefined offset %offset for object of class %class.', array
					(
						'%offset' => $offset,
						'%class' => get_class($container)
					)
				);
			}
			else if (is_array($container))
			{
				$message = format
				(
					'Undefined offset %offset for the array: !array', array
					(
						'%offset' => $offset,
						'!array' => $container
					)
				);
			}
			else
			{
				$message = format
				(
					'Undefined offset %offset.', array
					(
						'%offset' => $offset
					)
				);
			}
		}

		parent::__construct($message, $code, $previous);
	}
}

/**
 * Exception thrown when an array offset is not readable.
 */
class OffsetNotReadable extends OffsetError
{
	public function __construct($message, $code=500, \Exception $previous=null)
	{
		if (is_array($message))
		{
			list($offset, $container) = $message + array(1 => null);

			if (is_object($container))
			{
				$message = format
				(
					'The offset %offset for object of class %class is not readable.', array
					(
						'offset' => $offset,
						'class' => get_class($container)
					)
				);
			}
			else if (is_array($container))
			{
				$message = format
				(
					'The offset %offset is not readable for the array: !array', array
					(
						'offset' => $offset,
						'array' => $container
					)
				);
			}
			else
			{
				$message = format
				(
					'The offset %offset is not readable.', array
					(
						'offset' => $offset
					)
				);
			}
		}

		parent::__construct($message, $code, $previous);
	}
}

/**
 * Exception thrown when an array offset is not writable.
 */
class OffsetNotWritable extends OffsetError
{
	public function __construct($message, $code=500, \Exception $previous=null)
	{
		if (is_array($message))
		{
			list($offset, $container) = $message + array(1 => null);

			if (is_object($container))
			{
				$message = format
				(
					'The offset %offset for object of class %class is not writable.', array
					(
						'offset' => $offset,
						'class' => get_class($container)
					)
				);
			}
			else if (is_array($container))
			{
				$message = format
				(
					'The offset %offset is not writable for the array: !array', array
					(
						'offset' => $offset,
						'array' => $container
					)
				);
			}
			else
			{
				$message = format
				(
					'The offset %offset is not writable.', array
					(
						'offset' => $offset
					)
				);
			}
		}

		parent::__construct($message, $code, $previous);
	}
}

/**
 * Exception thrown when there is something wrong with an object property.
 *
 * This is the base class for property exceptions, one should rather use the
 * {@link PropertyNotDefined}, {@link PropertyNotReadable} or {@link PropertyNotWritable}
 * exceptions.
 */
class PropertyError extends \RuntimeException
{

}

/**
 * Exception thrown when a property is not defined.
 *
 * For example, this could be triggered by getting the value of an undefined property.
 */
class PropertyNotDefined extends PropertyError
{
	public function __construct($message, $code=500, \Exception $previous=null)
	{
		if (is_array($message))
		{
			list($property, $container) = $message + array(1 => null);

			if (is_object($container))
			{
				$message = format
				(
					'Undefined property %property for object of class %class.', array
					(
						'%property' => $property,
						'%class' => get_class($container)
					)
				);
			}
			else
			{
				$message = format
				(
					'Undefined property %property.', array
					(
						'%property' => $property
					)
				);
			}
		}

		parent::__construct($message, $code, $previous);
	}
}

/**
 * Exception thrown when a property is not readable.
 *
 * For example, this could be triggered when a private property is read from a public scope.
 */
class PropertyNotReadable extends PropertyError
{
	public function __construct($message, $code=500, \Exception $previous=null)
	{
		if (is_array($message))
		{
			list($property, $container) = $message + array(1 => null);

			if (is_object($container))
			{
				$message = format
				(
					'The property %property for object of class %class is not readable.', array
					(
						'%property' => $property,
						'%class' => get_class($container)
					)
				);
			}
			else
			{
				$message = format
				(
					'The property %property is not readable.', array
					(
						'%property' => $property
					)
				);
			}
		}

		parent::__construct($message, $code, $previous);
	}
}

/**
 * Exception thrown when a property is not writable.
 *
 * For example, this could be triggered when a private property is written from a public scope.
 */
class PropertyNotWritable extends PropertyError
{
	public function __construct($message, $code=500, \Exception $previous=null)
	{
		if (is_array($message))
		{
			list($property, $container) = $message + array(1 => null);

			if (is_object($container))
			{
				$message = format
				(
					'The property %property for object of class %class is not writable.', array
					(
						'%property' => $property,
						'%class' => get_class($container)
					)
				);
			}
			else
			{
				$message = format
				(
					'The property %property is not writable.', array
					(
						'%property' => $property
					)
				);
			}
		}

		parent::__construct($message, $code, $previous);
	}
}

/**
 * Exception thrown when a property has a reserved name.
 *
 * @property-read string $property Name of the reserved property.
 */
class PropertyIsReserved extends PropertyError
{
	private $property;

	public function __construct($property, $code=500, \Exception $previous=null)
	{
		$this->property = $property;

		parent::__construct(format('Property %property is reserved.', array('%property' => $property)), $code, $previous);
	}

	public function __get($property)
	{
		if ($property === 'property')
		{
			return $this->property;
		}

		throw new PropertyNotDefined(array($property, $this));
	}
}