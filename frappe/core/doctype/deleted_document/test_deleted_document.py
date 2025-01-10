# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Deleted Document')


class TestDeletedDocument(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDeletedDocument(UnitTestCase):
	"""
	Unit tests for DeletedDocument.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDeletedDocument(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
