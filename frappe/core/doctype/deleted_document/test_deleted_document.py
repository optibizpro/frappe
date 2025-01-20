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
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
