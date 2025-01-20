# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
from werkzeug.wrappers import Response

import frappe
from frappe.app import process_response
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

HEADERS = (
	"Access-Control-Allow-Origin",
	"Access-Control-Allow-Credentials",
	"Access-Control-Allow-Methods",
	"Access-Control-Allow-Headers",
	"Vary",
)


<<<<<<< HEAD
class TestCORS(FrappeTestCase):
=======
class TestCORS(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def make_request_and_test(self, origin="http://example.com", absent=False):
		self.origin = origin

		headers = {}
		if origin:
			headers = {
				"Origin": origin,
				"Access-Control-Request-Method": "POST",
				"Access-Control-Request-Headers": "X-Test-Header",
			}

		frappe.utils.set_request(method="OPTIONS", headers=headers)

		self.response = Response()
		process_response(self.response)

		for header in HEADERS:
			if absent:
				self.assertNotIn(header, self.response.headers)
			else:
				if header == "Access-Control-Allow-Origin":
					self.assertEqual(self.response.headers.get(header), self.origin)
				else:
					self.assertIn(header, self.response.headers)

	def test_cors_disabled(self):
		frappe.conf.allow_cors = None
		self.make_request_and_test("http://example.com", True)

	def test_request_without_origin(self):
		frappe.conf.allow_cors = "http://example.com"
		self.make_request_and_test(None, True)

	def test_valid_origin(self):
		frappe.conf.allow_cors = "http://example.com"
		self.make_request_and_test()

		frappe.conf.allow_cors = "*"
		self.make_request_and_test()

		frappe.conf.allow_cors = ["http://example.com", "https://example.com"]
		self.make_request_and_test()

	def test_invalid_origin(self):
		frappe.conf.allow_cors = "http://example1.com"
		self.make_request_and_test(absent=True)

		frappe.conf.allow_cors = ["http://example1.com", "https://example.com"]
		self.make_request_and_test(absent=True)
