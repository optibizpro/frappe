# Copyright (c) 2021, Frappe Technologies and contributors
# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class WebhookRequestLog(Document):
<<<<<<< HEAD
=======
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		data: DF.Code | None
		error: DF.Text | None
		headers: DF.Code | None
		reference_doctype: DF.Data | None
		reference_document: DF.Data | None
		response: DF.Code | None
		url: DF.Data | None
		user: DF.Link | None
		webhook: DF.Link | None
	# end: auto-generated types

>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	@staticmethod
	def clear_old_logs(days=30):
		from frappe.query_builder import Interval
		from frappe.query_builder.functions import Now

		table = frappe.qb.DocType("Webhook Request Log")
<<<<<<< HEAD
		frappe.db.delete(table, filters=(table.modified < (Now() - Interval(days=days))))
=======
		frappe.db.delete(table, filters=(table.creation < (Now() - Interval(days=days))))
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
