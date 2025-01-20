# Copyright (c) 2017, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestEmailRule(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestEmailRule(UnitTestCase):
	"""
	Unit tests for EmailRule.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestEmailRule(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
