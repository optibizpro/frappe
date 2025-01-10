# Copyright (c) 2021, Frappe Technologies and Contributors
# License: MIT. See LICENSE

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestWebhookRequestLog(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestWebhookRequestLog(UnitTestCase):
	"""
	Unit tests for WebhookRequestLog.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestWebhookRequestLog(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
