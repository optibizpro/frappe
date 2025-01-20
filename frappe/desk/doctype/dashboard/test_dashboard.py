# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
from frappe.config import get_modules_from_all_apps_for_user
from frappe.core.doctype.user.test_user import test_user
from frappe.tests.utils import FrappeTestCase


class TestDashboard(FrappeTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
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
<<<<<<< HEAD
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
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
