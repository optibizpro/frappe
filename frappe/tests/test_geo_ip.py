# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
from frappe.tests.utils import FrappeTestCase


class TestGeoIP(FrappeTestCase):
<<<<<<< HEAD
=======
from frappe.tests import IntegrationTestCase


class TestGeoIP(IntegrationTestCase):
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_geo_ip(self):
		return
		from frappe.sessions import get_geo_ip_country

		self.assertEqual(get_geo_ip_country("223.29.223.255"), "India")
		self.assertEqual(get_geo_ip_country("4.18.32.80"), "United States")
		self.assertEqual(get_geo_ip_country("217.194.147.25"), "United States")
