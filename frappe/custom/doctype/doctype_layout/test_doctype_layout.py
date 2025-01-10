# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDocTypeLayout(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDoctypeLayout(UnitTestCase):
	"""
	Unit tests for DoctypeLayout.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDocTypeLayout(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
