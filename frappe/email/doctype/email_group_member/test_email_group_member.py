# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Email Group Member')


class TestEmailGroupMember(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestEmailGroupMember(UnitTestCase):
	"""
	Unit tests for EmailGroupMember.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestEmailGroupMember(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
