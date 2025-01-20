# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
from frappe.config import get_modules_from_all_apps_for_user
from frappe.core.doctype.user.test_user import test_user
from frappe.tests.utils import FrappeTestCase


class TestDashboard(FrappeTestCase):
<<<<<<< HEAD
=======
=======
from frappe.core.doctype.user.test_user import test_user
from frappe.tests import IntegrationTestCase, UnitTestCase
from frappe.utils.modules import get_modules_from_all_apps_for_user


class UnitTestDashboard(UnitTestCase):
	"""
	Unit tests for Dashboard.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDashboard(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	def test_permission_query(self):
		for user in ["Administrator", "test@example.com"]:
			with self.set_user(user):
				frappe.get_list("Dashboard")

		with test_user(roles=["_Test Role"]) as user:
			with self.set_user(user.name):
				frappe.get_list("Dashboard")
				with self.set_user("Administrator"):
					all_modules = get_modules_from_all_apps_for_user("Administrator")
					for module in all_modules:
						user.append("block_modules", {"module": module.get("module_name")})
					user.save()
				frappe.get_list("Dashboard")
