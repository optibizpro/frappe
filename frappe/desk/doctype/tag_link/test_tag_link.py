# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestTagLink(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestTagLink(UnitTestCase):
	"""
	Unit tests for TagLink.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestTagLink(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
