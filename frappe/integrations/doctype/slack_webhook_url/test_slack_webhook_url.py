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
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	pass
