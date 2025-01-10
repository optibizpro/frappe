# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Unhandled Emails')


class TestUnhandledEmail(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestUnhandledEmail(UnitTestCase):
	"""
	Unit tests for UnhandledEmail.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestUnhandledEmail(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
