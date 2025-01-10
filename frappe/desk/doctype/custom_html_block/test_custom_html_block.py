# Copyright (c) 2023, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestCustomHTMLBlock(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestCustomHtmlBlock(UnitTestCase):
	"""
	Unit tests for CustomHtmlBlock.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestCustomHTMLBlock(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
