# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
"""
Events:
	always
	daily
	monthly
	weekly
"""

import datetime
import os
import random
import time
from typing import NoReturn

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
from croniter import CroniterBadCronError

# imports - module imports
=======
from croniter import CroniterBadCronError
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
from croniter import CroniterBadCronError
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
=======
import setproctitle
from croniter import CroniterBadCronError
from filelock import FileLock, Timeout
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
import frappe
<<<<<<< HEAD
from frappe.utils import cint, get_datetime, get_sites, now_datetime
from frappe.utils.background_jobs import get_jobs, set_niceness
=======
from frappe.utils import cint, get_bench_path, get_datetime, get_sites, now_datetime
from frappe.utils.background_jobs import set_niceness
from frappe.utils.caching import redis_cache
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_SCHEDULER_TICK = 4 * 60


def cprint(*args, **kwargs):
	"""Prints only if called from STDOUT"""
	try:
		os.get_terminal_size()
		print(*args, **kwargs)
	except Exception:
		pass


<<<<<<< HEAD
def start_scheduler():
=======
def _proctitle(message):
	setproctitle.setthreadtitle(f"frappe-scheduler: {message}")


def start_scheduler() -> NoReturn:
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	"""Run enqueue_events_for_all_sites based on scheduler tick.
	Specify scheduler_interval in seconds in common_site_config.json"""

	tick = get_scheduler_tick()
	set_niceness()
<<<<<<< HEAD

	while True:
		time.sleep(tick)
=======

	lock_path = os.path.abspath(os.path.join(get_bench_path(), "config", "scheduler_process"))

	try:
		lock = FileLock(lock_path)
		lock.acquire(blocking=False)
	except Timeout:
		frappe.logger("scheduler").debug("Scheduler already running")
		return

	while True:
		_proctitle("idle")
		time.sleep(sleep_duration(tick))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
		enqueue_events_for_all_sites()


def sleep_duration(tick):
	if tick != DEFAULT_SCHEDULER_TICK:
		# Assuming user knows what they want.
		return tick

	# Sleep until next multiple of tick.
	# This makes scheduler aligned with real clock,
	# so event scheduled at 12:00 happen at 12:00 and not 12:00:35.
	minutes = tick // 60
	now = datetime.datetime.now(datetime.timezone.utc)
	left_minutes = minutes - now.minute % minutes
	next_execution = now.replace(second=0) + datetime.timedelta(minutes=left_minutes)

	return (next_execution - now).total_seconds()


def enqueue_events_for_all_sites() -> None:
	"""Loop through sites and enqueue events that are not already queued"""

	with frappe.init_site():
		sites = get_sites()

	# Sites are sorted in alphabetical order, shuffle to randomize priorities
	random.shuffle(sites)

	for site in sites:
		try:
			enqueue_events_for_site(site=site)
		except Exception:
			frappe.logger("scheduler").debug(f"Failed to enqueue events for site: {site}", exc_info=True)


<<<<<<< HEAD
def enqueue_events_for_site(site):
	def log_and_raise():
		error_message = f"Exception in Enqueue Events for Site {site}\n{frappe.get_traceback()}"
		frappe.logger("scheduler").error(error_message)
=======
def enqueue_events_for_site(site: str) -> None:
	def log_exc():
		frappe.logger("scheduler").error(f"Exception in Enqueue Events for Site {site}", exc_info=True)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

	try:
		_proctitle(f"scheduling events for {site}")
		frappe.init(site)
		frappe.connect()
		if is_scheduler_inactive():
			return

		enqueue_events()

		frappe.logger("scheduler").debug(f"Queued events for site {site}")
	except Exception as e:
		if frappe.db.is_access_denied(e):
			frappe.logger("scheduler").debug(f"Access denied for site {site}")
		log_exc()

	finally:
		frappe.destroy()


def enqueue_events() -> list[str] | None:
	if schedule_jobs_based_on_activity():
<<<<<<< HEAD
		frappe.flags.enqueued_jobs = []
		queued_jobs = get_jobs(site=site, key="job_type").get(site) or []
		for job_type in frappe.get_all("Scheduled Job Type", ("name", "method"), dict(stopped=0)):
			if job_type.method not in queued_jobs:
				# don't add it to queue if still pending
				try:
					frappe.get_doc("Scheduled Job Type", job_type.name).enqueue()
				except CroniterBadCronError:
					frappe.logger("scheduler").error(
						f"Invalid Job on {frappe.local.site} - {job_type.name}", exc_info=True
					)
=======
		enqueued_jobs = []
		all_jobs = frappe.get_all("Scheduled Job Type", filters={"stopped": 0}, fields="*")
		random.shuffle(all_jobs)
		for job_type in all_jobs:
			job_type = frappe.get_doc(doctype="Scheduled Job Type", **job_type)
			try:
				if job_type.enqueue():
					enqueued_jobs.append(job_type.method)
			except CroniterBadCronError:
				frappe.logger("scheduler").error(
					f"Invalid Job on {frappe.local.site} - {job_type.name}", exc_info=True
				)

		return enqueued_jobs
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02


def is_scheduler_inactive(verbose=True) -> bool:
	if frappe.local.conf.maintenance_mode:
		if verbose:
			cprint(f"{frappe.local.site}: Maintenance mode is ON")
		return True

	if frappe.local.conf.pause_scheduler:
		if verbose:
			cprint(f"{frappe.local.site}: frappe.conf.pause_scheduler is SET")
		return True

	if is_scheduler_disabled(verbose=verbose):
		return True

	return False


def is_scheduler_disabled(verbose=True) -> bool:
	if frappe.conf.disable_scheduler:
		if verbose:
			cprint(f"{frappe.local.site}: frappe.conf.disable_scheduler is SET")
		return True

	scheduler_disabled = not frappe.utils.cint(
		frappe.db.get_single_value("System Settings", "enable_scheduler")
	)
	if scheduler_disabled:
		if verbose:
			cprint(f"{frappe.local.site}: SystemSettings.enable_scheduler is UNSET")
	return scheduler_disabled


def toggle_scheduler(enable):
	frappe.db.set_single_value("System Settings", "enable_scheduler", int(enable))


def enable_scheduler():
	toggle_scheduler(True)


def disable_scheduler():
	toggle_scheduler(False)


@redis_cache(ttl=60 * 60)
def schedule_jobs_based_on_activity(check_time=None):
	"""Return True for active sites as defined by `Activity Log`.
	Also return True for inactive sites once every 24 hours based on `Scheduled Job Log`."""
	if is_dormant(check_time=check_time):
		# ensure last job is one day old
<<<<<<< HEAD
		last_job_timestamp = _get_last_modified_timestamp("Scheduled Job Log")
=======
		last_job_timestamp = _get_last_creation_timestamp("Scheduled Job Log")
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
		if not last_job_timestamp:
			return True
		else:
			if ((check_time or now_datetime()) - last_job_timestamp).total_seconds() >= 86400:
				# one day is passed since jobs are run, so lets do this
				return True
			else:
				# schedulers run in the last 24 hours, do nothing
				return False
	else:
		# site active, lets run the jobs
		return True


def is_dormant(check_time=None):
	# Assume never dormant if developer_mode is enabled
	if frappe.conf.developer_mode:
		return False
<<<<<<< HEAD
	last_activity_log_timestamp = _get_last_modified_timestamp("Activity Log")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	last_activity_log_timestamp = _get_last_modified_timestamp("Activity Log")
=======
	last_activity_log_timestamp = _get_last_creation_timestamp("Activity Log")
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
	last_activity_log_timestamp = _get_last_creation_timestamp("Activity Log")
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
	last_activity_log_timestamp = _get_last_creation_timestamp("Activity Log")
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	since = (frappe.get_system_settings("dormant_days") or 4) * 86400
	if not last_activity_log_timestamp:
		return True
	if ((check_time or now_datetime()) - last_activity_log_timestamp).total_seconds() >= since:
		return True
	return False


<<<<<<< HEAD
def _get_last_modified_timestamp(doctype):
	timestamp = frappe.db.get_value(doctype, filters={}, fieldname="modified", order_by="modified desc")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def _get_last_modified_timestamp(doctype):
	timestamp = frappe.db.get_value(doctype, filters={}, fieldname="modified", order_by="modified desc")
=======
def _get_last_creation_timestamp(doctype):
	timestamp = frappe.db.get_value(doctype, filters={}, fieldname="creation", order_by="creation desc")
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
def _get_last_creation_timestamp(doctype):
	timestamp = frappe.db.get_value(doctype, filters={}, fieldname="creation", order_by="creation desc")
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
def _get_last_creation_timestamp(doctype):
	timestamp = frappe.db.get_value(doctype, filters={}, fieldname="creation", order_by="creation desc")
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	if timestamp:
		return get_datetime(timestamp)


@frappe.whitelist()
def activate_scheduler():
	from frappe.installer import update_site_config

	frappe.only_for("Administrator")

	if frappe.local.conf.maintenance_mode:
		frappe.throw(frappe._("Scheduler can not be re-enabled when maintenance mode is active."))

	if is_scheduler_disabled():
		enable_scheduler()
	if frappe.conf.pause_scheduler:
		update_site_config("pause_scheduler", 0)


@frappe.whitelist()
def get_scheduler_status():
	if is_scheduler_inactive():
		return {"status": "inactive"}
	return {"status": "active"}


def get_scheduler_tick() -> int:
<<<<<<< HEAD
	return cint(frappe.get_conf().scheduler_tick_interval) or 60
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	return cint(frappe.get_conf().scheduler_tick_interval) or 60
=======
	conf = frappe.get_conf()
	return cint(conf.scheduler_tick_interval) or DEFAULT_SCHEDULER_TICK
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
	conf = frappe.get_conf()
	return cint(conf.scheduler_tick_interval) or DEFAULT_SCHEDULER_TICK
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
	conf = frappe.get_conf()
	return cint(conf.scheduler_tick_interval) or DEFAULT_SCHEDULER_TICK
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
