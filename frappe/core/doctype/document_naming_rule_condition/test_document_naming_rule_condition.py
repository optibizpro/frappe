# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDocumentNamingRuleCondition(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDocumentNamingRuleCondition(UnitTestCase):
	"""
	Unit tests for DocumentNamingRuleCondition.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDocumentNamingRuleCondition(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
