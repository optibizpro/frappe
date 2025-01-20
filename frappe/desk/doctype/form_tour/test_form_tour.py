# Copyright (c) 2021, Frappe Technologies and Contributors
# License: MIT. See LICENSE

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestFormTour(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestFormTour(UnitTestCase):
	"""
	Unit tests for FormTour.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestFormTour(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
