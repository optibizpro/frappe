# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import os

import click

import frappe
from frappe.core.doctype.data_import.data_import import export_json, import_doc
from frappe.utils.deprecations import deprecation_warning


def sync_fixtures(app=None):
	"""Import, overwrite fixtures from `[app]/fixtures`"""
	if app:
		apps = [app]
	else:
		apps = frappe.get_installed_apps()

	frappe.flags.in_fixtures = True

	for app in apps:
		import_fixtures(app)
		import_custom_scripts(app)

	frappe.flags.in_fixtures = False


def import_fixtures(app):
	fixtures_path = frappe.get_app_path(app, "fixtures")
	if not os.path.exists(fixtures_path):
		return

	fixture_files = os.listdir(fixtures_path)

	for fname in fixture_files:
		if not fname.endswith(".json"):
			continue

		file_path = frappe.get_app_path(app, "fixtures", fname)
		try:
<<<<<<< HEAD
			import_doc(file_path)
=======
			import_doc(file_path, sort=True)
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		except (ImportError, frappe.DoesNotExistError) as e:
			# fixture syncing for missing doctypes
			print(f"Skipping fixture syncing from the file {fname}. Reason: {e}")


def import_custom_scripts(app):
	"""Import custom scripts from `[app]/fixtures/custom_scripts`"""
	scripts_folder = frappe.get_app_path(app, "fixtures", "custom_scripts")
	if not os.path.exists(scripts_folder):
		return

	for fname in os.listdir(scripts_folder):
		if not fname.endswith(".js"):
			continue

<<<<<<< HEAD
		doctype = fname.rsplit(".", 1)[0]
		if not frappe.db.exists("DocType", doctype):
			print(
				f"Skipping custom script fixture syncing for the missing doctype {doctype} from the file {fname}"
			)
			continue

		# not using get_app_path here as it scrubs the fname (will not work for dt name with > 1 word)
		file_path = scripts_folder + os.path.sep + fname
		deprecation_warning(
			f"Importing client script {fname} from {scripts_folder} is deprecated and will be removed in version-15. Use client scripts as fixtures directly."
		)

		with open(file_path) as f:
			script = f.read()
			if frappe.db.exists("Client Script", {"dt": doctype}):
				client_script = frappe.get_doc("Client Script", {"dt": doctype})
				client_script.script = script
				client_script.save()
			else:
				client_script = frappe.new_doc("Client Script")
				client_script.update({"__newname": doctype, "dt": doctype, "script": script})
				client_script.insert()
=======
		click.secho(
			f"Importing Client Script `{fname}` from `{scripts_folder}` is not supported. Convert the client script to fixture.",
			fg="red",
		)
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581


def export_fixtures(app=None):
	"""Export fixtures as JSON to `[app]/fixtures`"""
	if app:
		apps = [app]
	else:
		apps = frappe.get_installed_apps()
	for app in apps:
		fixture_auto_order = bool(next(iter(frappe.get_hooks("fixture_auto_order", app_name=app)), False))
		fixtures = frappe.get_hooks("fixtures", app_name=app)
		prefix = None
		for index, fixture in enumerate(fixtures, start=1):
			filters = None
			or_filters = None
			if isinstance(fixture, dict):
				filters = fixture.get("filters")
				or_filters = fixture.get("or_filters")
				prefix = fixture.get("prefix")
				fixture = fixture.get("doctype") or fixture.get("dt")
			print(f"Exporting {fixture} app {app} filters {(filters if filters else or_filters)}")
			if not os.path.exists(frappe.get_app_path(app, "fixtures")):
				os.mkdir(frappe.get_app_path(app, "fixtures"))

			filename = frappe.scrub(fixture)
			if prefix:
				filename = f"{prefix}_{filename}"
			if fixture_auto_order:
				number_of_digits = len(str(len(fixtures)))
				# add zero padding so files can be sorted lexicographically with filename.
				file_number = str(index).zfill(number_of_digits)
				filename = f"{file_number}_{filename}"

			export_json(
				fixture,
				frappe.get_app_path(app, "fixtures", filename + ".json"),
				filters=filters,
				or_filters=or_filters,
				order_by="idx asc, creation asc",
			)
