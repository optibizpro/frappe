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
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
