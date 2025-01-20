# Copyright (c) 2023, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestChangelogFeed(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestChangelogFeed(UnitTestCase):
	"""
	Unit tests for ChangelogFeed.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestChangelogFeed(IntegrationTestCase):
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
