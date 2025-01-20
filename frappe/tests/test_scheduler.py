import os
import time
from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import patch

import frappe
from frappe.core.doctype.scheduled_job_type.scheduled_job_type import ScheduledJobType, sync_jobs
from frappe.tests import IntegrationTestCase
from frappe.utils import add_days, get_datetime
<<<<<<< HEAD
from frappe.utils.doctor import purge_pending_jobs
from frappe.utils.scheduler import (
	_get_last_modified_timestamp,
	enqueue_events,
	is_dormant,
	schedule_jobs_based_on_activity,
=======
from frappe.utils.data import now_datetime
from frappe.utils.doctor import purge_pending_jobs
from frappe.utils.scheduler import (
	DEFAULT_SCHEDULER_TICK,
	_get_last_creation_timestamp,
	enqueue_events,
	is_dormant,
	schedule_jobs_based_on_activity,
	sleep_duration,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
)


def test_timeout_10():
	time.sleep(10)


def test_method():
	pass


class TestScheduler(IntegrationTestCase):
	def setUp(self):
		frappe.db.rollback()

		if not os.environ.get("CI"):
			return

		purge_pending_jobs()
		if not frappe.get_all("Scheduled Job Type", limit=1):
			sync_jobs()

	def tearDown(self):
		purge_pending_jobs()

	def test_enqueue_jobs(self):
		frappe.db.sql("update `tabScheduled Job Type` set last_execution = '2010-01-01 00:00:00'")

		enqueued_jobs = enqueue_events()

		self.assertIn("frappe.desk.notifications.clear_notifications", enqueued_jobs)
		self.assertIn("frappe.utils.change_log.check_for_update", enqueued_jobs)
		self.assertIn(
			"frappe.email.doctype.auto_email_report.auto_email_report.send_monthly",
			enqueued_jobs,
		)

	def test_queue_peeking(self):
		job = get_test_job()

		with patch.object(job, "is_job_in_queue", return_value=True):
			# 1st job is in the queue (or running), don't enqueue it again
			self.assertFalse(job.enqueue())

	def test_is_dormant(self):
		self.assertTrue(is_dormant(check_time=get_datetime("2100-01-01 00:00:00")))
		self.assertTrue(is_dormant(check_time=add_days(frappe.db.get_last_created("Activity Log"), 5)))
		self.assertFalse(is_dormant(check_time=frappe.db.get_last_created("Activity Log")))

	def test_once_a_day_for_dormant(self):
		frappe.db.truncate("Scheduled Job Log")
		self.assertTrue(schedule_jobs_based_on_activity(check_time=get_datetime("2100-01-01 00:00:00")))
		self.assertTrue(
			schedule_jobs_based_on_activity(
				check_time=add_days(frappe.db.get_last_created("Activity Log"), 5)
			)
		)

		# create a fake job executed 5 days from now
		job = get_test_job(method="frappe.tests.test_scheduler.test_method", frequency="Daily")
		job.execute()
		job_log = frappe.get_doc("Scheduled Job Log", dict(scheduled_job_type=job.name))
		job_log.db_set(
<<<<<<< HEAD
			"modified", add_days(_get_last_modified_timestamp("Activity Log"), 5), update_modified=False
		)
=======
			"creation", add_days(_get_last_creation_timestamp("Activity Log"), 5), update_modified=False
		)
		schedule_jobs_based_on_activity.clear_cache()
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

		# inactive site with recent job, don't run
		self.assertFalse(
			schedule_jobs_based_on_activity(
<<<<<<< HEAD
				check_time=add_days(_get_last_modified_timestamp("Activity Log"), 5)
=======
				check_time=add_days(_get_last_creation_timestamp("Activity Log"), 5)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
			)
		)

		# one more day has passed
		self.assertTrue(
			schedule_jobs_based_on_activity(
<<<<<<< HEAD
				check_time=add_days(_get_last_modified_timestamp("Activity Log"), 6)
=======
				check_time=add_days(_get_last_creation_timestamp("Activity Log"), 6)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
			)
		)

	def test_real_time_alignment(self):
		test_cases = {
			timedelta(minutes=0): DEFAULT_SCHEDULER_TICK,
			timedelta(minutes=0, seconds=12): DEFAULT_SCHEDULER_TICK - 12,
			timedelta(minutes=1, seconds=12): DEFAULT_SCHEDULER_TICK - (1 * 60 + 12),
			timedelta(hours=23, minutes=59): 60,
			timedelta(hours=23, minutes=59, seconds=30): 30,
			timedelta(minutes=0, seconds=1): DEFAULT_SCHEDULER_TICK - 1,
			timedelta(minutes=2): DEFAULT_SCHEDULER_TICK - 2 * 60,
		}
		for delta, expected_sleep in test_cases.items():
			fake_time = datetime(2024, 1, 1) + delta
			with self.freeze_time(fake_time, is_utc=True):
				self.assertEqual(sleep_duration(DEFAULT_SCHEDULER_TICK), expected_sleep, delta)

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======

>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======

>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
def get_test_job(method="frappe.tests.test_scheduler.test_timeout_10", frequency="All") -> ScheduledJobType:
	if not frappe.db.exists("Scheduled Job Type", dict(method=method)):
		job = frappe.get_doc(
			doctype="Scheduled Job Type",
			method=method,
			last_execution="2010-01-01 00:00:00",
			frequency=frequency,
		).insert()
	else:
		job = frappe.get_doc("Scheduled Job Type", dict(method=method))
		job.db_set("last_execution", "2010-01-01 00:00:00")
		job.db_set("frequency", frequency)
	frappe.db.commit()

	return job
