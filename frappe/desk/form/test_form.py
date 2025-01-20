# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe
from frappe.desk.form.linked_with import get_linked_docs, get_linked_doctypes
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestForm(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase


class TestForm(IntegrationTestCase):
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	def test_linked_with(self):
		results = get_linked_docs("Role", "System Manager", linkinfo=get_linked_doctypes("Role"))
		self.assertTrue("User" in results)
		self.assertTrue("DocType" in results)
<<<<<<< HEAD


if __name__ == "__main__":
	import unittest

	frappe.connect()
	unittest.main()
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
