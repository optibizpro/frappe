# Copyright (c) 2015, Frappe Technologies and contributors
# License: MIT. See LICENSE

import frappe
from frappe import _
from frappe.model.document import Document


class OAuthProviderSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		skip_authorization: DF.Literal["Force", "Auto"]
	# end: auto-generated types

	pass


def get_oauth_settings():
<<<<<<< HEAD
	"""Returns oauth settings"""
	out = frappe._dict(
=======
	"""Return OAuth settings."""
	return frappe._dict(
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		{"skip_authorization": frappe.db.get_single_value("OAuth Provider Settings", "skip_authorization")}
	)
