# Copyright (c) 2018, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestSlackWebhookURL(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestSlackWebhookUrl(UnitTestCase):
	"""
	Unit tests for SlackWebhookUrl.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestSlackWebhookURL(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
