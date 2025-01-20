# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt


from frappe.core.report.database_storage_usage_by_tables.database_storage_usage_by_tables import (
	execute,
)
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDBUsageReport(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase


class TestDBUsageReport(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_basic_query(self):
		_, data = execute()
		tables = [d.table for d in data]
		self.assertFalse({"tabUser", "tabDocField"}.difference(tables))
