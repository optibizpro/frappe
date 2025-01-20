# Copyright (c) 2021, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPackageRelease(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPackageRelease(UnitTestCase):
	"""
	Unit tests for PackageRelease.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPackageRelease(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
