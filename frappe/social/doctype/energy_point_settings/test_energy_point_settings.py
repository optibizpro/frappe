# Copyright (c) 2021, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestEnergyPointSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestEnergyPointSettings(UnitTestCase):
	"""
	Unit tests for EnergyPointSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestEnergyPointSettings(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
