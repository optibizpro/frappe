# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import os

no_cache = 1

import json
import re
from urllib.parse import urlencode

import frappe
import frappe.sessions
from frappe import _
from frappe.utils.jinja_globals import is_rtl

SCRIPT_TAG_PATTERN = re.compile(r"\<script[^<]*\</script\>")
CLOSING_SCRIPT_TAG_PATTERN = re.compile(r"</script\>")


def get_context(context):
	if frappe.session.user == "Guest":
		frappe.response["status_code"] = 403
		frappe.msgprint(_("Log in to access this page."))
		frappe.redirect(f"/login?{urlencode({'redirect-to': frappe.request.path})}")
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======

>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	elif frappe.db.get_value("User", frappe.session.user, "user_type", order_by=None) == "Website User":
=======

	elif frappe.session.data.user_type == "Website User":
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
		frappe.throw(_("You are not permitted to access this page."), frappe.PermissionError)

	try:
		boot = frappe.sessions.get()
	except Exception as e:
		raise frappe.SessionBootFailed from e

	# this needs commit
	csrf_token = frappe.sessions.get_csrf_token()

	frappe.db.commit()

<<<<<<< HEAD
	boot_json = frappe.as_json(boot, indent=None, separators=(",", ":"))

	# remove script tags from boot
	boot_json = SCRIPT_TAG_PATTERN.sub("", boot_json)

	# TODO: Find better fix
	boot_json = CLOSING_SCRIPT_TAG_PATTERN.sub("", boot_json)

<<<<<<< HEAD
	include_js = hooks.get("app_include_js", []) + frappe.conf.get("app_include_js", [])
	include_css = hooks.get("app_include_css", []) + frappe.conf.get("app_include_css", [])
	include_icons = hooks.get("app_include_icons", [])
	frappe.local.preload_assets["icons"].extend(include_icons)

	if frappe.get_system_settings("enable_telemetry") and os.getenv("FRAPPE_SENTRY_DSN"):
		include_js.append("sentry.bundle.js")
=======
=======
>>>>>>> c72e91f4653d639300c4d8d8a7951c2aa8a95c2c
	hooks = frappe.get_hooks()
	app_include_js = hooks.get("app_include_js", []) + frappe.conf.get("app_include_js", [])
	app_include_css = hooks.get("app_include_css", []) + frappe.conf.get("app_include_css", [])
	app_include_icons = hooks.get("app_include_icons", [])

	if frappe.get_system_settings("enable_telemetry") and os.getenv("FRAPPE_SENTRY_DSN"):
		app_include_js.append("sentry.bundle.js")
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b

	include_js = hooks.get("app_include_js", []) + frappe.conf.get("app_include_js", [])
	include_css = hooks.get("app_include_css", []) + frappe.conf.get("app_include_css", [])

	context.update(
		{
			"no_cache": 1,
			"build_version": frappe.utils.get_build_version(),
<<<<<<< HEAD
			"include_js": include_js,
			"include_css": include_css,
=======
			"app_include_js": app_include_js,
			"app_include_css": app_include_css,
			"app_include_icons": app_include_icons,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
			"layout_direction": "rtl" if is_rtl() else "ltr",
			"lang": frappe.local.lang,
			"sounds": hooks["sounds"],
			"boot": boot,
			"desk_theme": boot.get("desk_theme") or "Light",
			"csrf_token": csrf_token,
			"google_analytics_id": frappe.conf.get("google_analytics_id"),
			"google_analytics_anonymize_ip": frappe.conf.get("google_analytics_anonymize_ip"),
			"app_name": (
				frappe.get_website_settings("app_name") or frappe.get_system_settings("app_name") or "Frappe"
			),
		}
	)

	return context
