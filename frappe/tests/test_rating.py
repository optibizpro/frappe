import frappe
from frappe.core.doctype.doctype.test_doctype import new_doctype
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestRating(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase


class TestRating(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	def setUp(self):
		doc = new_doctype(
			fields=[
				{
					"fieldname": "rating",
					"fieldtype": "Rating",
					"label": "rating",
					"reqd": 1,  # mandatory
				},
			],
		)
		doc.insert()
		self.doctype_name = doc.name

	def test_negative_rating(self):
<<<<<<< HEAD
		doc = frappe.get_doc(doctype=self.doctype_name, rating=-1)
=======
		doc = frappe.new_doc(doctype=self.doctype_name, rating=-1)
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		doc.insert()
		self.assertEqual(doc.rating, 0)

	def test_positive_rating(self):
<<<<<<< HEAD
		doc = frappe.get_doc(doctype=self.doctype_name, rating=5)
=======
		doc = frappe.new_doc(doctype=self.doctype_name, rating=5)
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		doc.insert()
		self.assertEqual(doc.rating, 1)
