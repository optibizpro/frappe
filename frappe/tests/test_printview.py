import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
from frappe.www.printview import get_html_and_style


class PrintViewTest(FrappeTestCase):
=======
from frappe.core.doctype.doctype.test_doctype import new_doctype
<<<<<<< HEAD
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
=======
from frappe.tests import IntegrationTestCase
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
from frappe.www.printview import get_html_and_style


class PrintViewTest(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_print_view_without_errors(self):
		user = frappe.get_last_doc("User")

		messages_before = frappe.get_message_log()
		ret = get_html_and_style(doc=user.as_json(), print_format="Standard", no_letterhead=1)
		messages_after = frappe.get_message_log()

		if len(messages_after) > len(messages_before):
			new_messages = messages_after[len(messages_before) :]
			self.fail("Print view showing error/warnings: \n" + "\n".join(str(msg) for msg in new_messages))

		# html should exist
		self.assertTrue(bool(ret["html"]))

	def test_print_error(self):
		"""Print failures shouldn't generate PDF with failure message but instead escalate the error"""
		doctype = new_doctype(is_submittable=1).insert()

		doc = frappe.new_doc(doctype.name)
		doc.insert()
		doc.submit()
		doc.cancel()

		# cancelled doc can't be printed by default
		self.assertRaises(frappe.PermissionError, frappe.attach_print, doc.doctype, doc.name)
