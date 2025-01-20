# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestAboutUsSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestAboutUsSettings(UnitTestCase):
	"""
	Unit tests for AboutUsSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestAboutUsSettings(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
