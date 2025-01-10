# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.config import get_modules_from_all_apps_for_user
from frappe.tests.utils import FrappeTestCase


class TestConfig(FrappeTestCase):
	def test_get_modules(self):
		frappe_modules = frappe.get_all("Module Def", filters={"app_name": "frappe"}, pluck="name")
		all_modules_data = get_modules_from_all_apps_for_user()
		first_module_entry = all_modules_data[0]
		all_modules = [x["module_name"] for x in all_modules_data]
		self.assertIn("links", first_module_entry)
=======
from frappe.tests import IntegrationTestCase
from frappe.utils.modules import get_modules_from_all_apps_for_user


class TestConfig(IntegrationTestCase):
	def test_get_modules(self):
		frappe_modules = frappe.get_all("Module Def", filters={"app_name": "frappe"}, pluck="name")
		all_modules_data = get_modules_from_all_apps_for_user()
		all_modules = [x["module_name"] for x in all_modules_data]
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		self.assertIsInstance(all_modules_data, list)
		self.assertFalse([x for x in frappe_modules if x not in all_modules])
