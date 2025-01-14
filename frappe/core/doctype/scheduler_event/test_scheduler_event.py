# Copyright (c) 2025, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests import IntegrationTestCase, UnitTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestSchedulerEvent(UnitTestCase):
	"""
	Unit tests for SchedulerEvent.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestSchedulerEvent(IntegrationTestCase):
	"""
	Integration tests for SchedulerEvent.
	Use this class for testing interactions between multiple components.
	"""

=======
from frappe.tests.utils import FrappeTestCase


class TestSchedulerEvent(FrappeTestCase):
>>>>>>> 3eda272bd61b1e73b74d30b1704d885a39c75d0c
	pass
