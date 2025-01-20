# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestBlogCategory(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestBlogCategory(UnitTestCase):
	"""
	Unit tests for BlogCategory.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestBlogCategory(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
