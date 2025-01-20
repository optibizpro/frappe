# Copyright (c) 2020, Frappe Technologies and contributors
# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class ConsoleLog(Document):
<<<<<<< HEAD
=======
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		committed: DF.Check
		script: DF.Code | None
		type: DF.Data | None
	# end: auto-generated types

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def after_delete(self):
		# because on_trash can be bypassed
		frappe.throw(frappe._("Console Logs can not be deleted"))
