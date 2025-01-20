# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import json

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
from frappe.utils import add_to_date, get_link_to_form, today
from frappe.utils.data import is_html


class UnitTestAutoEmailReport(UnitTestCase):
	"""
	Unit tests for AutoEmailReport.
	Use this class for testing individual functions and methods.
	"""

	pass


<<<<<<< HEAD
class TestAutoEmailReport(FrappeTestCase):
=======
class TestAutoEmailReport(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_auto_email(self):
		frappe.delete_doc("Auto Email Report", "Permitted Documents For User")

		auto_email_report = get_auto_email_report()

		data = auto_email_report.get_report_content()

		self.assertTrue(is_html(data))
		self.assertTrue(str(get_link_to_form("Module Def", "Core")) in data)

		auto_email_report.format = "CSV"

		data = auto_email_report.get_report_content()
		self.assertTrue('"Language","Core"' in data)

		auto_email_report.format = "XLSX"

		data = auto_email_report.get_report_content()

	def test_dynamic_date_filters(self):
		auto_email_report = get_auto_email_report()

		auto_email_report.dynamic_date_period = "Weekly"
		auto_email_report.from_date_field = "from_date"
		auto_email_report.to_date_field = "to_date"

		auto_email_report.prepare_dynamic_filters()

		self.assertEqual(auto_email_report.filters["from_date"], add_to_date(today(), weeks=-1))
		self.assertEqual(auto_email_report.filters["to_date"], today())


def get_auto_email_report():
	if not frappe.db.exists("Auto Email Report", "Permitted Documents For User"):
		auto_email_report = frappe.get_doc(
			doctype="Auto Email Report",
			report="Permitted Documents For User",
			report_type="Script Report",
			user="Administrator",
			enabled=1,
			email_to="test@example.com",
			format="HTML",
			frequency="Daily",
			filters=json.dumps(dict(user="Administrator", doctype="DocType")),
		).insert()
	else:
		auto_email_report = frappe.get_doc("Auto Email Report", "Permitted Documents For User")

	return auto_email_report
