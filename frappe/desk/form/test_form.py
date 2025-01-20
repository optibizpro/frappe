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
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
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
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
