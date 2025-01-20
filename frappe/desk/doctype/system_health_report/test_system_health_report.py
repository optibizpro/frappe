# Copyright (c) 2024, Frappe Technologies and Contributors
# See license.txt

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
from frappe.tests.utils import FrappeTestCase


class TestSystemHealthReport(FrappeTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestSystemHealthReport(UnitTestCase):
	"""
	Unit tests for SystemHealthReport.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestSystemHealthReport(IntegrationTestCase):
<<<<<<< HEAD
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_it_works(self):
		frappe.get_doc("System Health Report")
