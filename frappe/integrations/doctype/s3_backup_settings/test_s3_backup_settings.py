# Copyright (c) 2017, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestS3BackupSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestS3BackupSettings(UnitTestCase):
	"""
	Unit tests for S3BackupSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestS3BackupSettings(IntegrationTestCase):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	pass
