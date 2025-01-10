# Copyright (c) 2024, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPermissionInspector(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPermissionInspector(UnitTestCase):
	"""
	Unit tests for PermissionInspector.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPermissionInspector(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
