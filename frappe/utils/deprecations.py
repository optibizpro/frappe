<<<<<<< HEAD
""" Utils for deprecating functionality in Framework.
=======
"""Utils for deprecating functionality in Framework.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

WARNING: This file is internal, instead of depending just copy the code or use deprecation
libraries.
"""
<<<<<<< HEAD
import functools
import warnings


def deprecated(func):
	"""Decorator to wrap a function/method as deprecated."""

	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		deprecation_warning(
			f"{func.__name__} is deprecated and will be removed in next major version.",
			stacklevel=1,
		)
		return func(*args, **kwargs)

	return wrapper


def deprecation_warning(message, category=DeprecationWarning, stacklevel=1):
	"""like warnings.warn but with auto incremented sane stacklevel."""

	warnings.warn(message=message, category=category, stacklevel=stacklevel + 2)
=======

from frappe.deprecation_dumpster import (
	_old_deprecated as deprecated,
)
from frappe.deprecation_dumpster import (
	_old_deprecation_warning as deprecation_warning,
)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
