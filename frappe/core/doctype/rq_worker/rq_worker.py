# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import datetime
from contextlib import suppress

<<<<<<< HEAD
=======
import pytz
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
from rq import Worker

import frappe
from frappe.model.document import Document
from frappe.utils import cint, convert_utc_to_system_timezone
from frappe.utils.background_jobs import get_workers


class RQWorker(Document):
<<<<<<< HEAD
=======
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		birth_date: DF.Datetime | None
		current_job_id: DF.Link | None
		failed_job_count: DF.Int
		last_heartbeat: DF.Datetime | None
		pid: DF.Data | None
		queue: DF.Data | None
		queue_type: DF.Literal["default", "long", "short"]
		status: DF.Data | None
		successful_job_count: DF.Int
		total_working_time: DF.Duration | None
		utilization_percent: DF.Percent
		worker_name: DF.Data | None
	# end: auto-generated types

<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
	def load_from_db(self):
		all_workers = get_workers()
		workers = [w for w in all_workers if w.name == self.name]
		if not workers:
			raise frappe.DoesNotExistError
		d = serialize_worker(workers[0])

		super(Document, self).__init__(d)

	@staticmethod
<<<<<<< HEAD
	def get_list(args):
		start = cint(args.get("start")) or 0
		page_length = cint(args.get("page_length")) or 20

=======
	def get_list(start=0, page_length=20):
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		workers = get_workers()

		valid_workers = [w for w in workers if w.pid][start : start + page_length]
		return [serialize_worker(worker) for worker in valid_workers]

	@staticmethod
<<<<<<< HEAD
	def get_count(args) -> int:
=======
	def get_count() -> int:
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		return len(get_workers())

	# None of these methods apply to virtual workers, overriden for sanity.
	@staticmethod
<<<<<<< HEAD
	def get_stats(args):
=======
	def get_stats():
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		return {}

	def db_insert(self, *args, **kwargs):
		pass

	def db_update(self, *args, **kwargs):
		pass

	def delete(self):
		pass


def serialize_worker(worker: Worker) -> frappe._dict:
	queue_names = worker.queue_names()

	queue = ", ".join(queue_names)
	queue_types = ",".join(q.rsplit(":", 1)[1] for q in queue_names)

<<<<<<< HEAD
=======
	current_job = worker.get_current_job_id()
	if current_job and not current_job.startswith(frappe.local.site):
		current_job = None

<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
	return frappe._dict(
		name=worker.name,
		queue=queue,
		queue_type=queue_types,
		worker_name=worker.name,
		status=worker.get_state(),
		pid=worker.pid,
<<<<<<< HEAD
		current_job_id=worker.get_current_job_id(),
=======
		current_job_id=current_job,
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		last_heartbeat=convert_utc_to_system_timezone(worker.last_heartbeat),
		birth_date=convert_utc_to_system_timezone(worker.birth_date),
		successful_job_count=worker.successful_job_count,
		failed_job_count=worker.failed_job_count,
		total_working_time=worker.total_working_time,
		_comment_count=0,
		modified=convert_utc_to_system_timezone(worker.last_heartbeat),
		creation=convert_utc_to_system_timezone(worker.birth_date),
		utilization_percent=compute_utilization(worker),
	)


def compute_utilization(worker: Worker) -> float:
	with suppress(Exception):
<<<<<<< HEAD
		total_time = (datetime.datetime.utcnow() - worker.birth_date).total_seconds()
=======
		total_time = (
<<<<<<< HEAD
			datetime.datetime.now(pytz.UTC) - worker.birth_date.replace(tzinfo=pytz.UTC)
=======
			datetime.datetime.now(datetime.timezone.utc)
			- worker.birth_date.replace(tzinfo=datetime.timezone.utc)
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		).total_seconds()
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		return worker.total_working_time / total_time * 100
