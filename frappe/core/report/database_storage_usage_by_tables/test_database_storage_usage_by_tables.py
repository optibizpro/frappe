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
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	def test_basic_query(self):
		_, data = execute()
		tables = [d.table for d in data]
		self.assertFalse({"tabUser", "tabDocField"}.difference(tables))
