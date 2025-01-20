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
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
