# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe
import frappe.permissions
from frappe import _
from frappe.core.doctype.activity_log.activity_log import add_authentication_log
from frappe.utils import get_fullname


def login_feed(login_manager):
	if login_manager.user != "Guest":
		subject = _("{0} logged in").format(get_fullname(login_manager.user))
		add_authentication_log(subject, login_manager.user)


def logout_feed(user, reason):
	if user and user != "Guest":
		subject = _("{0} logged out: {1}").format(get_fullname(user), frappe.bold(reason))
		add_authentication_log(subject, user, operation="Logout")
<<<<<<< HEAD


def get_feed_match_conditions(user=None, doctype="Comment"):
	if not user:
		user = frappe.session.user

	conditions = [
		"`tab{doctype}`.owner={user} or `tab{doctype}`.reference_owner={user}".format(
			user=frappe.db.escape(user), doctype=doctype
		)
	]

	user_permissions = frappe.permissions.get_user_permissions(user)
	can_read = frappe.get_user().get_can_read()

	can_read_doctypes = [f"'{dt}'" for dt in list(set(can_read) - set(list(user_permissions)))]

	if can_read_doctypes:
		conditions += [
			"""(`tab{doctype}`.reference_doctype is null
			or `tab{doctype}`.reference_doctype = ''
			or `tab{doctype}`.reference_doctype
			in ({values}))""".format(doctype=doctype, values=", ".join(can_read_doctypes))
		]

		if user_permissions:
			can_read_docs = []
			for dt, obj in user_permissions.items():
				for n in obj:
					can_read_docs.append(
						"{}|{}".format(frappe.db.escape(dt), frappe.db.escape(n.get("doc", "")))
					)

			if can_read_docs:
				conditions.append(
					"concat_ws('|', `tab{doctype}`.reference_doctype, `tab{doctype}`.reference_name) in ({values})".format(
						doctype=doctype, values=", ".join(can_read_docs)
					)
				)

	return "(" + " or ".join(conditions) + ")"
=======
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
