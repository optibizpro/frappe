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
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
