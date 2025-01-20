# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('OAuth Authorization Code')


class TestOAuthAuthorizationCode(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestOauthAuthorizationCode(UnitTestCase):
	"""
	Unit tests for OauthAuthorizationCode.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestOAuthAuthorizationCode(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
