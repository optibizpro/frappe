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
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
