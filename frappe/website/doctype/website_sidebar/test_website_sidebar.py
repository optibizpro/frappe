# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Website Sidebar')


class TestWebsiteSidebar(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestWebsiteSidebar(UnitTestCase):
	"""
	Unit tests for WebsiteSidebar.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestWebsiteSidebar(IntegrationTestCase):
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
