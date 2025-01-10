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
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
