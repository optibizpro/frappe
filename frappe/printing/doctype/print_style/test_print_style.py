# Copyright (c) 2017, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPrintStyle(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPrintStyle(UnitTestCase):
	"""
	Unit tests for PrintStyle.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPrintStyle(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
