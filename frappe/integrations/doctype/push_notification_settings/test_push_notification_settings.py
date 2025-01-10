# Copyright (c) 2024, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPushNotificationSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPushNotificationSettings(UnitTestCase):
	"""
	Unit tests for PushNotificationSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPushNotificationSettings(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
