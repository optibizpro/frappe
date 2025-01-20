# Copyright (c) 2019, Frappe Technologies and contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase, UnitTestCase
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

EXTRA_TEST_RECORD_DEPENDENCIES = ["User", "Connected App", "Token Cache"]


<<<<<<< HEAD
class TestTokenCache(FrappeTestCase):
=======
class UnitTestTokenCache(UnitTestCase):
	"""
	Unit tests for TokenCache.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestTokenCache(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def setUp(self):
		self.token_cache = frappe.get_last_doc("Token Cache")
		self.token_cache.update({"connected_app": frappe.get_last_doc("Connected App").name})
		self.token_cache.save(ignore_permissions=True)

	def test_get_auth_header(self):
		self.token_cache.get_auth_header()

	def test_update_data(self):
		self.token_cache.update_data(
			{
				"access_token": "new-access-token",
				"refresh_token": "new-refresh-token",
				"token_type": "bearer",
				"expires_in": 2000,
				"scope": "new scope",
			}
		)

	def test_get_expires_in(self):
		self.token_cache.get_expires_in()

	def test_is_expired(self):
		self.token_cache.is_expired()

	def get_json(self):
		self.token_cache.get_json()
