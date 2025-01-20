# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestLogSettingUser(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestLogSettingUser(UnitTestCase):
	"""
	Unit tests for LogSettingUser.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestLogSettingUser(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
