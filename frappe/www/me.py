# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe
import frappe.www.list
from frappe import _

no_cache = 1


def get_context(context):
	if frappe.session.user == "Guest":
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

	context.current_user = frappe.get_doc("User", frappe.session.user)
<<<<<<< HEAD
	context.show_sidebar = True
=======
	context.show_sidebar = False
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
