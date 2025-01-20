# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestAddressTemplate(FrappeTestCase):
	def setUp(self):
		self.make_default_address_template()
=======
from frappe.contacts.doctype.address_template.address_template import get_default_address_template
from frappe.tests import IntegrationTestCase, UnitTestCase
from frappe.utils.jinja import validate_template


class UnitTestAddressTemplate(UnitTestCase):
	"""
	Unit tests for AddressTemplate.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestAddressTemplate(IntegrationTestCase):
	def setUp(self) -> None:
		frappe.db.delete("Address Template", {"country": "India"})
		frappe.db.delete("Address Template", {"country": "Brazil"})

	def test_default_address_template(self):
		validate_template(get_default_address_template())
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

	def test_default_is_unset(self):
		frappe.get_doc({"doctype": "Address Template", "country": "India", "is_default": 1}).insert()

		self.assertEqual(frappe.db.get_value("Address Template", "India", "is_default"), 1)

		frappe.get_doc({"doctype": "Address Template", "country": "Brazil", "is_default": 1}).insert()

		self.assertEqual(frappe.db.get_value("Address Template", "India", "is_default"), 0)
		self.assertEqual(frappe.db.get_value("Address Template", "Brazil", "is_default"), 1)

	def test_delete_address_template(self):
		india = frappe.get_doc({"doctype": "Address Template", "country": "India", "is_default": 0}).insert()

		brazil = frappe.get_doc(
			{"doctype": "Address Template", "country": "Brazil", "is_default": 1}
		).insert()

		india.reload()  # might have been modified by the second template
		india.delete()  # should not raise an error

		self.assertRaises(frappe.ValidationError, brazil.delete)
