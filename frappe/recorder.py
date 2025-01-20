# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
import datetime
=======
import cProfile
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
import functools
import inspect
import io
import json
import pstats
import re
import time
from collections import Counter
from collections.abc import Callable
<<<<<<< HEAD
=======
from dataclasses import dataclass
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df

import sqlparse

import frappe
from frappe import _
from frappe.database.database import is_query_type
from frappe.utils import now_datetime

RECORDER_INTERCEPT_FLAG = "recorder-intercept"
RECORDER_CONFIG_FLAG = "recorder-config"
RECORDER_REQUEST_SPARSE_HASH = "recorder-requests-sparse"
RECORDER_REQUEST_HASH = "recorder-requests"
TRACEBACK_PATH_PATTERN = re.compile(".*/apps/")
RECORDER_AUTO_DISABLE = 5 * 60


@dataclass
class RecorderConfig:
	record_requests: bool = True  # Record web request
	record_jobs: bool = True  # record background jobs
	record_sql: bool = True  # Record SQL queries
	capture_stack: bool = True  # Recod call stack of SQL queries
	profile: bool = False  # Run cProfile
	explain: bool = True  # Provide explain output of SQL queries
	request_filter: str = "/"  # Filter request paths
	jobs_filter: str = ""  # Filter background jobs

	def __post_init__(self):
		if not (self.record_jobs or self.record_requests):
			frappe.throw("You must record one of jobs or requests")

	def store(self):
		frappe.cache.set_value(RECORDER_CONFIG_FLAG, self, expires_in_sec=RECORDER_AUTO_DISABLE)

	@classmethod
	def retrieve(cls):
		return frappe.cache.get_value(RECORDER_CONFIG_FLAG) or cls()

	@staticmethod
	def delete():
		frappe.cache.delete_value(RECORDER_CONFIG_FLAG)


def record_sql(*args, **kwargs):
	start_time = time.monotonic()
	result = frappe.db._sql(*args, **kwargs)
	end_time = time.monotonic()

<<<<<<< HEAD
	stack = list(get_current_stack_frames())

	data = {
		"query": str(frappe.db.last_query),
=======
	query = getattr(frappe.db, "last_query", None)
	if not query or isinstance(result, str):
		# run=0, doesn't actually run the query so last_query won't be present
		return result

	stack = []
	if frappe.local._recorder.config.capture_stack:
		stack = list(get_current_stack_frames())

	data = {
		"query": str(query),
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		"stack": stack,
		"explain_result": [],
		"time": start_time,
		"duration": float(f"{(end_time - start_time) * 1000:.3f}"),
	}

	frappe.local._recorder.register(data)
	return result


def get_current_stack_frames():
	from frappe.utils.safe_exec import SERVER_SCRIPT_FILE_PREFIX

	try:
		current = inspect.currentframe()
		frames = inspect.getouterframes(current, context=10)
<<<<<<< HEAD
		for _frame, filename, lineno, function, _context, _index in list(reversed(frames))[:-2]:
			if "/apps/" in filename or "<serverscript>" in filename:
=======
		for frame, filename, lineno, function, context, index in list(reversed(frames))[:-2]:  # noqa: B007
			if "/apps/" in filename or SERVER_SCRIPT_FILE_PREFIX in filename:
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
				yield {
					"filename": TRACEBACK_PATH_PATTERN.sub("", filename),
					"lineno": lineno,
					"function": function,
				}
	except Exception:
		pass


def post_process():
	"""post process all recorded values.

	Any processing that can be done later should be done here to avoid overhead while
	profiling. As of now following values are post-processed:
	        - `EXPLAIN` output of queries.
	        - SQLParse reformatting of queries
	        - Mark duplicates
	"""
	frappe.db.rollback()
	frappe.db.begin(read_only=True)  # Explicitly start read only transaction

<<<<<<< HEAD
	result = list(frappe.cache().hgetall(RECORDER_REQUEST_HASH).values())
=======
	config = RecorderConfig.retrieve()
	result = list(frappe.cache.hgetall(RECORDER_REQUEST_HASH).values())
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df

	for request in result:
		for call in request["calls"]:
			formatted_query = sqlparse.format(
				call["query"].strip(), keyword_case="upper", reindent=True, strip_comments=True
			)
			call["query"] = formatted_query

			# Collect EXPLAIN for executed query
<<<<<<< HEAD
			if is_query_type(formatted_query, ("select", "update", "delete")):
=======
			if config.explain and is_query_type(formatted_query, ("select", "update", "delete")):
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
				# Only SELECT/UPDATE/DELETE queries can be "EXPLAIN"ed
				try:
					call["explain_result"] = frappe.db.sql(f"EXPLAIN {formatted_query}", as_dict=True)
				except Exception:
					pass
		mark_duplicates(request)
<<<<<<< HEAD
		frappe.cache().hset(RECORDER_REQUEST_HASH, request["uuid"], request)
=======
		frappe.cache.hset(RECORDER_REQUEST_HASH, request["uuid"], request)

	config.delete()
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df


def mark_duplicates(request):
	exact_duplicates = Counter([call["query"] for call in request["calls"]])

	for sql_call in request["calls"]:
		sql_call["normalized_query"] = normalize_query(sql_call["query"])

	normalized_duplicates = Counter([call["normalized_query"] for call in request["calls"]])

	for index, call in enumerate(request["calls"]):
		call["index"] = index
		call["exact_copies"] = exact_duplicates[call["query"]]
		call["normalized_copies"] = normalized_duplicates[call["normalized_query"]]


def normalize_query(query: str) -> str:
	"""Attempt to normalize query by removing variables.
	This gives a different view of similar duplicate queries.

	Example:
	        These two are distinct queries:
	                `select * from user where name = 'x'`
	                `select * from user where name = 'z'`

	        But their "normalized" form would be same:
	                `select * from user where name = ?`
	"""

	try:
		q = sqlparse.parse(query)[0]
		for token in q.flatten():
			if "Token.Literal" in str(token.ttype):
				token.value = "?"

		# Transform IN parts like this: IN (?, ?, ?) -> IN (?)
		q = re.sub(r"( IN )\(\?[\s\n\?\,]*\)", r"\1(?)", str(q), flags=re.IGNORECASE)
		return q
	except Exception as e:
		print("Failed to normalize query ", e)

	return query


def record(force=False):
<<<<<<< HEAD
	if __debug__:
		if frappe.cache().get_value(RECORDER_INTERCEPT_FLAG) or force:
			frappe.local._recorder = Recorder()
=======
<<<<<<< HEAD
<<<<<<< HEAD
	if __debug__:
		if frappe.cache.get_value(RECORDER_INTERCEPT_FLAG) or force:
			frappe.local._recorder = Recorder(force=force)
=======
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
	flag_value = frappe.client_cache.get_value(RECORDER_INTERCEPT_FLAG)
	if flag_value or force:
		frappe.local._recorder = Recorder(force=force)
	elif flag_value is None:
		# Explicitly set it once so next requests can use client-side cache
		frappe.client_cache.set_value(RECORDER_INTERCEPT_FLAG, False)
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df


def dump():
	if hasattr(frappe.local, "_recorder"):
		frappe.local._recorder.dump()


class Recorder:
	def __init__(self, force=False):
		self.config = RecorderConfig.retrieve()
		self.calls = []
<<<<<<< HEAD
		if frappe.request:
=======
		self._patched_sql = False
		self.profiler = None
		self._recording = True
		self.force = force
		self.cmd = None
		self.method = None
		self.headers = None
		self.form_dict = None

		if (
			self.config.record_requests
			and frappe.request
			and self.config.request_filter in frappe.request.path
		):
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
			self.path = frappe.request.path
			self.cmd = frappe.local.form_dict.cmd or ""
			self.method = frappe.request.method
			self.headers = dict(frappe.local.request.headers)
			self.form_dict = frappe.local.form_dict
<<<<<<< HEAD
		else:
			self.path = None
=======
			self.event_type = "HTTP Request"
		elif self.config.record_jobs and frappe.job and self.config.jobs_filter in frappe.job.method:
			self.event_type = "Background Job"
			self.path = frappe.job.method
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
			self.cmd = None
			self.method = None
			self.headers = None
			self.form_dict = None
<<<<<<< HEAD

		_patch()
=======
		elif not self.force:
			self._recording = False
			return
		else:
			self.event_type = "Function Call"

		self.uuid = frappe.generate_hash(length=10)
		self.time = now_datetime()

		if self.config.record_sql:
			self._patch_sql()
			self._patched_sql = True

		if self.config.profile:
			self.profiler = cProfile.Profile()
			self.profiler.enable()
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df

	def register(self, data):
		self.calls.append(data)

	def cleanup(self):
		if self.profiler:
			self.profiler.disable()
		if self._patched_sql:
			self._unpatch_sql()

	def process_profiler(self):
		if self.config.profile or self.profiler:
			self.profiler.disable()
			profiler_output = io.StringIO()
			pstats.Stats(self.profiler, stream=profiler_output).strip_dirs().sort_stats(
				"cumulative"
			).print_stats()
			profile = profiler_output.getvalue()
			profiler_output.close()
			return profile

	def dump(self):
		if not self._recording:
			return
		profiler_output = self.process_profiler()

		request_data = {
			"uuid": self.uuid,
			"path": self.path,
			"cmd": self.cmd,
			"time": self.time,
			"queries": len(self.calls),
			"time_queries": float("{:0.3f}".format(sum(call["duration"] for call in self.calls))),
			"duration": float(f"{(now_datetime() - self.time).total_seconds() * 1000:0.3f}"),
			"method": self.method,
			"event_type": self.event_type,
		}
<<<<<<< HEAD
		frappe.cache().hset(RECORDER_REQUEST_SPARSE_HASH, self.uuid, request_data)
		frappe.publish_realtime(
			event="recorder-dump-event",
			message=json.dumps(request_data, default=str),
			user="Administrator",
		)
=======
		frappe.cache.hset(RECORDER_REQUEST_SPARSE_HASH, self.uuid, request_data)
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df

		request_data["calls"] = self.calls
		request_data["headers"] = self.headers
		request_data["form_dict"] = self.form_dict
		request_data["profile"] = profiler_output
		frappe.cache.hset(RECORDER_REQUEST_HASH, self.uuid, request_data)

<<<<<<< HEAD
=======
		if self.config.record_sql:
			self._unpatch_sql()

	@staticmethod
	def _patch_sql():
		frappe.db._sql = frappe.db.sql
		frappe.db.sql = record_sql
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df

	@staticmethod
	def _unpatch_sql():
		frappe.db.sql = frappe.db._sql


def _unpatch():
	frappe.db.sql = frappe.db._sql


def do_not_record(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		if hasattr(frappe.local, "_recorder"):
			frappe.local._recorder.cleanup()
			del frappe.local._recorder
		return function(*args, **kwargs)

	return wrapper


def administrator_only(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		if frappe.session.user != "Administrator":
			frappe.throw(_("Only Administrator is allowed to use Recorder"))
		return function(*args, **kwargs)

	return wrapper


@frappe.whitelist()
@do_not_record
@administrator_only
def status(*args, **kwargs):
	return bool(frappe.cache.get_value(RECORDER_INTERCEPT_FLAG))


@frappe.whitelist()
@do_not_record
@administrator_only
<<<<<<< HEAD
def start(*args, **kwargs):
	frappe.cache().set_value(RECORDER_INTERCEPT_FLAG, 1, expires_in_sec=60 * 60)
=======
def start(
	record_jobs: bool = True,
	record_requests: bool = True,
	record_sql: bool = True,
	profile: bool = False,
	capture_stack: bool = True,
	explain: bool = True,
	request_filter: str = "/",
	jobs_filter: str = "",
	*args,
	**kwargs,
):
	RecorderConfig(
		record_requests=int(record_requests),
		record_jobs=int(record_jobs),
		record_sql=int(record_sql),
		profile=int(profile),
		capture_stack=int(capture_stack),
		explain=int(explain),
		request_filter=request_filter,
		jobs_filter=jobs_filter,
	).store()
<<<<<<< HEAD
	frappe.cache.set_value(RECORDER_INTERCEPT_FLAG, 1, expires_in_sec=RECORDER_AUTO_DISABLE)
=======
	frappe.client_cache.set_value(RECORDER_INTERCEPT_FLAG, True)
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df


@frappe.whitelist()
@do_not_record
@administrator_only
def stop(*args, **kwargs):
<<<<<<< HEAD
	frappe.cache().delete_value(RECORDER_INTERCEPT_FLAG)
=======
<<<<<<< HEAD
<<<<<<< HEAD
	frappe.cache.delete_value(RECORDER_INTERCEPT_FLAG)
=======
	frappe.client_cache.set_value(RECORDER_INTERCEPT_FLAG, False)
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
	frappe.client_cache.set_value(RECORDER_INTERCEPT_FLAG, False)
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
	frappe.enqueue(post_process, now=frappe.flags.in_test)


@frappe.whitelist()
@do_not_record
@administrator_only
def get(uuid=None, *args, **kwargs):
	if uuid:
		result = frappe.cache.hget(RECORDER_REQUEST_HASH, uuid)
	else:
		result = list(frappe.cache.hgetall(RECORDER_REQUEST_SPARSE_HASH).values())
	return result


@frappe.whitelist()
@do_not_record
@administrator_only
def export_data(*args, **kwargs):
	return list(frappe.cache.hgetall(RECORDER_REQUEST_HASH).values())


@frappe.whitelist()
@do_not_record
@administrator_only
def delete(*args, **kwargs):
<<<<<<< HEAD
	frappe.cache().delete_value(RECORDER_REQUEST_SPARSE_HASH)
	frappe.cache().delete_value(RECORDER_REQUEST_HASH)
=======
	frappe.cache.delete_value(RECORDER_REQUEST_SPARSE_HASH)
	frappe.cache.delete_value(RECORDER_REQUEST_HASH)
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df


def record_queries(func: Callable):
	"""Decorator to profile a specific function using recorder."""

	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		record(force=True)
		frappe.local._recorder.path = f"Function call: {func.__module__}.{func.__qualname__}"
		ret = func(*args, **kwargs)
		dump()
<<<<<<< HEAD
		_unpatch()
=======
		Recorder._unpatch_sql()
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		post_process()
		print("Recorded queries, open recorder to view them.")
		return ret

	return wrapped
<<<<<<< HEAD
=======


@frappe.whitelist()
@do_not_record
@administrator_only
def import_data(file: str) -> None:
	file_doc = frappe.get_doc("File", {"file_url": file})
	file_content = json.loads(file_doc.get_content())
	for request in file_content:
		frappe.cache.hset(RECORDER_REQUEST_SPARSE_HASH, request["uuid"], request)
		frappe.cache.hset(RECORDER_REQUEST_HASH, request["uuid"], request)
	file_doc.delete(delete_permanently=True)
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
