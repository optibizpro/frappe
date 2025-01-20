from urllib.parse import quote_plus

import frappe
from frappe import _
from frappe.utils import cstr
from frappe.website.page_renderers.template_page import TemplatePage


class NotPermittedPage(TemplatePage):
	def __init__(self, path=None, http_status_code=None, exception=""):
		frappe.local.message = cstr(exception)
		super().__init__(path=path, http_status_code=http_status_code)
		self.http_status_code = 403

	def can_render(self):
		return True

	def render(self):
<<<<<<< HEAD
		action = f"/login?redirect-to={frappe.request.path}"
<<<<<<< HEAD
<<<<<<< HEAD
		if frappe.request.path.startswith("/app"):
=======
		if frappe.request.path.startswith("/app/") or frappe.request.path == "/app":
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
		if frappe.request.path.startswith("/app"):
=======
		action = f"/login?redirect-to={quote_plus(frappe.request.path)}"
		if frappe.request.path.startswith("/app/") or frappe.request.path == "/app":
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
			action = "/login"
		frappe.local.message_title = _("Not Permitted")
		frappe.local.response["context"] = dict(
			indicator_color="red", primary_action=action, primary_label=_("Login"), fullpage=True
		)
		self.set_standard_path("message")
		return super().render()
