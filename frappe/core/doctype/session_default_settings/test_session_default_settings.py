# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
from frappe.core.doctype.session_default_settings.session_default_settings import (
	clear_session_defaults,
	set_session_default_values,
)
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestSessionDefaultSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestSessionDefaultSettings(UnitTestCase):
	"""
	Unit tests for SessionDefaultSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestSessionDefaultSettings(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_set_session_default_settings(self):
		frappe.set_user("Administrator")
		settings = frappe.get_single("Session Default Settings")
		settings.session_defaults = []
		settings.append("session_defaults", {"ref_doctype": "Role"})
		settings.save()

		set_session_default_values({"role": "Website Manager"})

		todo = frappe.get_doc(
			doctype="ToDo", description="test session defaults set", assigned_by="Administrator"
		).insert()
		self.assertEqual(todo.role, "Website Manager")

	def test_clear_session_defaults(self):
		clear_session_defaults()
		todo = frappe.get_doc(
			doctype="ToDo", description="test session defaults cleared", assigned_by="Administrator"
		).insert()
		self.assertNotEqual(todo.role, "Website Manager")
