# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('OAuth Bearer Token')


class TestOAuthBearerToken(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestOauthBearerToken(UnitTestCase):
	"""
	Unit tests for OauthBearerToken.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestOAuthBearerToken(IntegrationTestCase):
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
