# Copyright (c) 2021, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPackageImport(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPackageImport(UnitTestCase):
	"""
	Unit tests for PackageImport.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPackageImport(IntegrationTestCase):
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
