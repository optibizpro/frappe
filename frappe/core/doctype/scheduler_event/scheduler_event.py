# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SchedulerEvent(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		method: DF.Data | None
<<<<<<< HEAD
		scheduled_against: DF.Link
=======
		scheduled_against: DF.Link | None
>>>>>>> 3eda272bd61b1e73b74d30b1704d885a39c75d0c
	# end: auto-generated types

	pass
