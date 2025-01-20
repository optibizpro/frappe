# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# License: MIT. See LICENSE

<<<<<<< HEAD
import os
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
from contextlib import suppress

import redis

import frappe
from frappe.utils.data import cstr


def publish_progress(percent, title=None, doctype=None, docname=None, description=None, task_id=None):
	publish_realtime(
		"progress",
		{"percent": percent, "title": title, "description": description},
		user=None if doctype and docname else frappe.session.user,
		doctype=doctype,
		docname=docname,
		task_id=task_id,
	)


def publish_realtime(
	event: str | None = None,
	message: dict | None = None,
	room: str | None = None,
	user: str | None = None,
	doctype: str | None = None,
	docname: str | None = None,
	task_id: str | None = None,
	after_commit: bool = False,
):
	"""Publish real-time updates

	:param event: Event name, like `task_progress` etc. that will be handled by the client (default is `task_progress` if within task or `global`)
	:param message: JSON message object. For async must contain `task_id`
	:param room: Room in which to publish update (default entire site)
	:param user: Transmit to user
	:param doctype: Transmit to doctype, docname
	:param docname: Transmit to doctype, docname
	:param after_commit: (default False) will emit after current transaction is committed"""
	if message is None:
		message = {}

<<<<<<< HEAD
	if event is None:
		event = "task_progress" if frappe.local.task_id else "global"
=======
	if not task_id and hasattr(frappe.local, "task_id"):
		task_id = frappe.local.task_id

	if event is None:
		event = "task_progress" if task_id else "global"
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	elif event == "msgprint" and not user:
		user = frappe.session.user
	elif event == "list_update":
		doctype = doctype or message.get("doctype")
		room = get_doctype_room(doctype)
	elif event == "docinfo_update":
		room = get_doc_room(doctype, docname)
<<<<<<< HEAD

	if not task_id and hasattr(frappe.local, "task_id"):
		task_id = frappe.local.task_id
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

	if not room:
		if task_id:
			after_commit = False
			if "task_id" not in message:
				message["task_id"] = task_id
			room = get_task_progress_room(task_id)
		elif user:
			# transmit to specific user: System, Website or Guest
			room = get_user_room(user)
		elif doctype and docname:
			room = get_doc_room(doctype, docname)
		else:
			# This will be broadcasted to all Desk users
			room = get_site_room()

	if after_commit:
		if not hasattr(frappe.local, "_realtime_log"):
			frappe.local._realtime_log = []
			frappe.db.after_commit.add(flush_realtime_log)
			frappe.db.after_rollback.add(clear_realtime_log)

		params = [event, message, room]
		if params not in frappe.local._realtime_log:
			frappe.local._realtime_log.append(params)
	else:
		emit_via_redis(event, message, room)


def flush_realtime_log():
	for args in frappe.local._realtime_log:
		frappe.realtime.emit_via_redis(*args)

	clear_realtime_log()


def clear_realtime_log():
	if hasattr(frappe.local, "_realtime_log"):
		del frappe.local._realtime_log


def emit_via_redis(event, message, room):
	"""Publish real-time updates via redis

	:param event: Event name, like `task_progress` etc.
	:param message: JSON message object. For async must contain `task_id`
	:param room: name of the room"""
<<<<<<< HEAD

	with suppress(redis.exceptions.ConnectionError):
		r = get_redis_server()
		r.publish("events", frappe.as_json({"event": event, "message": message, "room": room}))


def get_redis_server():
	"""returns redis_socketio connection."""
	global redis_server
	if not redis_server:
		from redis import Redis

		redis_server = Redis.from_url(frappe.conf.redis_socketio or "redis://localhost:12311")
	return redis_server


@frappe.whitelist(allow_guest=True)
def can_subscribe_doc(doctype, docname):
	if os.environ.get("CI"):
		return True

	from frappe.exceptions import PermissionError

	if not frappe.has_permission(doctype=doctype, doc=docname, ptype="read"):
		raise PermissionError()

	return True


@frappe.whitelist(allow_guest=True)
def can_subscribe_doctype(doctype: str) -> bool:
	from frappe.exceptions import PermissionError

	if not frappe.has_permission(doctype=doctype, ptype="read"):
		raise PermissionError()
=======
	from frappe.utils.background_jobs import get_redis_connection_without_auth

	with suppress(redis.exceptions.ConnectionError):
		r = get_redis_connection_without_auth()
		r.publish(
			"events",
			frappe.as_json(
				{"event": event, "message": message, "room": room, "namespace": frappe.local.site}
			),
		)


@frappe.whitelist(allow_guest=True)
def has_permission(doctype: str, name: str) -> bool:
	if not frappe.has_permission(doctype=doctype, doc=name, ptype="read"):
		raise frappe.PermissionError
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

	return True


@frappe.whitelist(allow_guest=True)
def get_user_info():
	return {
		"user": frappe.session.user,
		"user_type": frappe.session.data.user_type,
<<<<<<< HEAD
=======
		"installed_apps": frappe.get_installed_apps(),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	}


def get_doctype_room(doctype):
<<<<<<< HEAD
	return f"{frappe.local.site}:doctype:{doctype}"


def get_doc_room(doctype, docname):
	return f"{frappe.local.site}:doc:{doctype}/{cstr(docname)}"


def get_user_room(user):
	return f"{frappe.local.site}:user:{user}"


def get_site_room():
	return f"{frappe.local.site}:all"


def get_task_progress_room(task_id):
	return f"{frappe.local.site}:task_progress:{task_id}"


def get_website_room():
	return f"{frappe.local.site}:website"
=======
	return f"doctype:{doctype}"


def get_doc_room(doctype, docname):
	return f"doc:{doctype}/{cstr(docname)}"


def get_user_room(user):
	return f"user:{user}"


def get_site_room():
	return "all"


def get_task_progress_room(task_id):
	return f"task_progress:{task_id}"


def get_website_room():
	return "website"
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
