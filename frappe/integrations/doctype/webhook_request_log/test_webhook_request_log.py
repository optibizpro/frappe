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
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	pass
