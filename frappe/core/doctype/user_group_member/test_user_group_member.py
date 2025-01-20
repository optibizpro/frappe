# Copyright (c) 2021, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestUserGroupMember(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestUserGroupMember(UnitTestCase):
	"""
	Unit tests for UserGroupMember.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestUserGroupMember(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
