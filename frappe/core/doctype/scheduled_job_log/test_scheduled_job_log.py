# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestScheduledJobLog(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestScheduledJobLog(UnitTestCase):
	"""
	Unit tests for ScheduledJobLog.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestScheduledJobLog(IntegrationTestCase):
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
