# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDropboxSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDropboxSettings(UnitTestCase):
	"""
	Unit tests for DropboxSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDropboxSettings(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
