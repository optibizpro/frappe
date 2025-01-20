# Copyright (c) 2021, Frappe Technologies and Contributors
# License: MIT. See LICENSE

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestWorkflowAction(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestWorkflowAction(UnitTestCase):
	"""
	Unit tests for WorkflowAction.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestWorkflowAction(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
