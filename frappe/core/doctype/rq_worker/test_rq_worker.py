# Copyright (c) 2022, Frappe Technologies and Contributors
# See license.txt

import frappe
from frappe.core.doctype.rq_worker.rq_worker import RQWorker
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestRQWorker(FrappeTestCase):
	def test_get_worker_list(self):
		workers = RQWorker.get_list({})
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestRqWorker(UnitTestCase):
	"""
	Unit tests for RqWorker.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestRQWorker(IntegrationTestCase):
	def test_get_worker_list(self):
		workers = RQWorker.get_list()
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		self.assertGreaterEqual(len(workers), 1)
		self.assertTrue(any("short" in w.queue_type for w in workers))

	def test_worker_serialization(self):
<<<<<<< HEAD
		workers = RQWorker.get_list({})
=======
		workers = RQWorker.get_list()
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		frappe.get_doc("RQ Worker", workers[0].name)
