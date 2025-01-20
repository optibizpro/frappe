# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestConsoleLog(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestConsoleLog(UnitTestCase):
	"""
	Unit tests for ConsoleLog.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestConsoleLog(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
