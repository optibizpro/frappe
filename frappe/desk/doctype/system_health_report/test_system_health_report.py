# Copyright (c) 2024, Frappe Technologies and Contributors
# See license.txt

import frappe
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
from frappe.tests.utils import FrappeTestCase


class TestSystemHealthReport(FrappeTestCase):
<<<<<<< HEAD
=======
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestSystemHealthReport(UnitTestCase):
	"""
	Unit tests for SystemHealthReport.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestSystemHealthReport(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	def test_it_works(self):
		frappe.get_doc("System Health Report")
