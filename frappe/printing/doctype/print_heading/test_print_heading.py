# Copyright (c) 2017, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPrintHeading(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPrintHeading(UnitTestCase):
	"""
	Unit tests for PrintHeading.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPrintHeading(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
