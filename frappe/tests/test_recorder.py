# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

<<<<<<< HEAD
=======
import time
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

import sqlparse

import frappe
import frappe.recorder
from frappe.recorder import normalize_query
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase, timeout
=======
from frappe.tests import IntegrationTestCase, timeout
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
from frappe.tests import IntegrationTestCase, timeout
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
from frappe.tests import IntegrationTestCase, timeout
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
from frappe.utils import set_request
from frappe.utils.doctor import any_job_pending
from frappe.website.serve import get_response_content


<<<<<<< HEAD
class TestRecorder(FrappeTestCase):
=======
class TestRecorder(IntegrationTestCase):
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
		self.wait_for_background_jobs()
		frappe.recorder.stop()
		frappe.recorder.delete()
		set_request()
		frappe.recorder.start()
		frappe.recorder.record()

<<<<<<< HEAD
=======
	@timeout
	def wait_for_background_jobs(self):
		while any_job_pending(frappe.local.site):
			time.sleep(1)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def stop_recording(self):
		frappe.recorder.dump()
		frappe.recorder.stop()

	def test_start(self):
		self.stop_recording()
		requests = frappe.recorder.get()
		self.assertEqual(len(requests), 1)

	def test_do_not_record(self):
		frappe.recorder.do_not_record(frappe.get_all)("DocType")
		self.stop_recording()
		requests = frappe.recorder.get()
		self.assertEqual(len(requests), 0)

	def test_get(self):
		self.stop_recording()

		requests = frappe.recorder.get()
		self.assertEqual(len(requests), 1)

		request = frappe.recorder.get(requests[0]["uuid"])
		self.assertTrue(request)

	def test_delete(self):
		self.stop_recording()

		requests = frappe.recorder.get()
		self.assertEqual(len(requests), 1)

		frappe.recorder.delete()

		requests = frappe.recorder.get()
		self.assertEqual(len(requests), 0)

	def test_record_without_sql_queries(self):
		self.stop_recording()

		requests = frappe.recorder.get()
		request = frappe.recorder.get(requests[0]["uuid"])

		self.assertEqual(len(request["calls"]), 0)

	def test_record_with_sql_queries(self):
		frappe.get_all("DocType")
		self.stop_recording()

		requests = frappe.recorder.get()
		request = frappe.recorder.get(requests[0]["uuid"])

		self.assertNotEqual(len(request["calls"]), 0)

	def test_explain(self):
		frappe.db.sql("SELECT * FROM tabDocType")
		frappe.db.sql("COMMIT")
<<<<<<< HEAD
=======
		frappe.db.sql("select 1", run=0)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
		self.stop_recording()

		requests = frappe.recorder.get()
		request = frappe.recorder.get(requests[0]["uuid"])

		self.assertEqual(len(request["calls"][0]["explain_result"]), 1)
		self.assertEqual(len(request["calls"][1]["explain_result"]), 0)

	def test_multiple_queries(self):
		queries = [
			{"mariadb": "SELECT * FROM tabDocType", "postgres": 'SELECT * FROM "tabDocType"'},
			{"mariadb": "SELECT COUNT(*) FROM tabDocType", "postgres": 'SELECT COUNT(*) FROM "tabDocType"'},
			{"mariadb": "COMMIT", "postgres": "COMMIT"},
		]

		sql_dialect = frappe.db.db_type or "mariadb"
		for query in queries:
			frappe.db.sql(query[sql_dialect])

		self.stop_recording()

		requests = frappe.recorder.get()
		request = frappe.recorder.get(requests[0]["uuid"])

		self.assertEqual(len(request["calls"]), len(queries))

		for query, call in zip(queries, request["calls"], strict=False):
			self.assertEqual(
				call["query"],
				sqlparse.format(
					query[sql_dialect].strip(), keyword_case="upper", reindent=True, strip_comments=True
				),
			)

	def test_duplicate_queries(self):
		queries = [
			("SELECT * FROM tabDocType", 2),
			("SELECT COUNT(*) FROM tabDocType", 1),
			("select * from tabDocType", 2),
			("COMMIT", 3),
			("COMMIT", 3),
			("COMMIT", 3),
		]
		for query in queries:
			frappe.db.sql(query[0])

		self.stop_recording()

		requests = frappe.recorder.get()
		request = frappe.recorder.get(requests[0]["uuid"])

		for query, call in zip(queries, request["calls"], strict=False):
			self.assertEqual(call["exact_copies"], query[1])

	def test_error_page_rendering(self):
		content = get_response_content("error")
		self.assertIn("Error", content)


<<<<<<< HEAD
class TestRecorderDeco(FrappeTestCase):
=======
class TestRecorderDeco(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_recorder_flag(self):
		frappe.recorder.delete()

		@frappe.recorder.record_queries
		def test():
			frappe.get_all("User")

		test()
		self.assertTrue(frappe.recorder.get())


<<<<<<< HEAD
class TestQueryNormalization(FrappeTestCase):
=======
class TestQueryNormalization(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_query_normalization(self):
		test_cases = {
			"select * from user where name = 'x'": "select * from user where name = ?",
			"select * from user where a > 5": "select * from user where a > ?",
			"select * from `user` where a > 5": "select * from `user` where a > ?",
			"select `name` from `user`": "select `name` from `user`",
			"select `name` from `user` limit 10": "select `name` from `user` limit ?",
			"select `name` from `user` where name in ('a', 'b', 'c')": "select `name` from `user` where name in (?)",
		}

		for query, normalized in test_cases.items():
			self.assertEqual(normalize_query(query), normalized)
