# Copyright (c) 2021, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestNetworkPrinterSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestNetworkPrinterSettings(UnitTestCase):
	"""
	Unit tests for NetworkPrinterSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestNetworkPrinterSettings(IntegrationTestCase):
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
