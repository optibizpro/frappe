# Copyright (c) 2017, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestLetterHead(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestLetterHead(UnitTestCase):
	"""
	Unit tests for LetterHead.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestLetterHead(IntegrationTestCase):
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	def test_auto_image(self):
		letter_head = frappe.get_doc(
			doctype="Letter Head", letter_head_name="Test", source="Image", image="/public/test.png"
		).insert()

		# test if image is automatically set
		self.assertTrue(letter_head.image in letter_head.content)
