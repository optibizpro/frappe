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
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
