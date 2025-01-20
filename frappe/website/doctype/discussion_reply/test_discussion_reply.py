# Copyright (c) 2021, FOSS United and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDiscussionReply(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDiscussionReply(UnitTestCase):
	"""
	Unit tests for DiscussionReply.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDiscussionReply(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
