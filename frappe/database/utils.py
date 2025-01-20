# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

<<<<<<< HEAD
from functools import cached_property, wraps
=======
<<<<<<< HEAD
import typing
from functools import cached_property, wraps
from types import NoneType
=======
from functools import cached_property, wraps
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581

import frappe
from frappe.query_builder.builder import MariaDB, Postgres
from frappe.query_builder.functions import Function
<<<<<<< HEAD

Query = str | MariaDB | Postgres
QueryValues = tuple | list | dict | None
=======
from frappe.types import DocRef

Query = str | MariaDB | Postgres
QueryValues = tuple | list | dict | None
<<<<<<< HEAD
=======
FilterValue = DocRef | str | int | bool
<<<<<<< HEAD
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

EmptyQueryValues = object()
FallBackDateTimeStr = "0001-01-01 00:00:00.000000"
DefaultOrderBy = "KEEP_DEFAULT_ORDERING"
NestedSetHierarchy = (
	"ancestors of",
	"descendants of",
	"not ancestors of",
	"not descendants of",
<<<<<<< HEAD
=======
	"descendants of (inclusive)",
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
)


def convert_to_value(o: FilterValue):
	if hasattr(o, "__value__"):
		return o.__value__()
	if isinstance(o, bool):
		return int(o)
	return o


def is_query_type(query: str, query_type: str | tuple[str, ...]) -> bool:
	return query.lstrip().split(maxsplit=1)[0].lower().startswith(query_type)


def is_pypika_function_object(field: str) -> bool:
	return getattr(field, "__module__", None) == "pypika.functions" or isinstance(field, Function)


def get_doctype_name(table_name: str) -> str:
	if table_name.startswith(("tab", "`tab", '"tab')):
		table_name = table_name.replace("tab", "", 1)
	table_name = table_name.replace("`", "")
<<<<<<< HEAD
	table_name = table_name.replace('"', "")
	return table_name
=======
	return table_name.replace('"', "")
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02


class LazyString:
	def _setup(self) -> str:
		raise NotImplementedError

	@cached_property
	def value(self) -> str:
		return self._setup()

	def __str__(self) -> str:
		return self.value

	def __repr__(self) -> str:
		return f"'{self.value}'"


class LazyDecode(LazyString):
	__slots__ = ()

	def __init__(self, value: str) -> None:
		self._value = value

	def _setup(self) -> str:
		return self._value.decode()


class LazyMogrify(LazyString):
	__slots__ = ()

	def __init__(self, query, values) -> None:
		self.query = query
		self.values = values

	def _setup(self) -> str:
		return frappe.db.mogrify(self.query, self.values)


def dangerously_reconnect_on_connection_abort(func):
	"""Reconnect on connection failure.

	As the name suggest, it's dangerous to use this function as it will NOT restore DB transaction
	so make sure you're using it right.

	Ideal use case: Some kinda logging or final steps in a background jobs. Anything more than that
	will risk bugs from DB transactions.
	"""

	@wraps(func)
	def wrapper(*args, **kwargs):
		try:
			return func(*args, **kwargs)
		except Exception as e:
			if frappe.db.is_interface_error(e):
				frappe.db.connect()
				return func(*args, **kwargs)
			raise

	return wrapper
