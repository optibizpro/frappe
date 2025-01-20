import os
import sys

import click

import click

import frappe
from frappe.database.db_manager import DbManager


def get_mariadb_variables():
	return frappe._dict(frappe.db.sql("show variables"))


def get_mariadb_version(version_string: str = ""):
	# MariaDB classifies their versions as Major (1st and 2nd number), and Minor (3rd number)
	# Example: Version 10.3.13 is Major Version = 10.3, Minor Version = 13
	version_string = version_string or get_mariadb_variables().get("version")
<<<<<<< HEAD
	version = version_string.split("-")[0]
=======
	version = version_string.split("-", 1)[0]
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	return version.rsplit(".", 1)


def setup_database(force, verbose, mariadb_user_host_login_scope=None):
	frappe.local.session = frappe._dict({"user": "Administrator"})

	db_user = frappe.conf.db_user
	db_name = frappe.local.conf.db_name
	root_conn = get_root_connection()
	dbman = DbManager(root_conn)
	dbman_kwargs = {}

	if mariadb_user_host_login_scope is not None:
		dbman_kwargs["host"] = mariadb_user_host_login_scope
<<<<<<< HEAD
=======

	dbman.create_user(db_user, frappe.conf.db_password, **dbman_kwargs)
	if verbose:
		print(f"Created or updated user {db_user}")
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b

	if force or (db_name not in dbman.get_database_list()):
		dbman.drop_database(db_name)
	else:
		print(f"Database {db_name} already exists, please drop it manually or pass `--force`.")
		sys.exit(1)

	dbman.create_database(db_name)
	if verbose:
		print("Created database {}".format(db_name))

	dbman.grant_all_privileges(db_name, db_user, **dbman_kwargs)
	dbman.flush_privileges()
	if verbose:
		print(f"Granted privileges to user {db_user} and database {db_name}")

	# close root connection
	root_conn.close()

<<<<<<< HEAD
	bootstrap_database(db_name, verbose, source_sql)


def setup_help_database(help_db_name):
	dbman = DbManager(get_root_connection(frappe.flags.root_login, frappe.flags.root_password))
	dbman.drop_database(help_db_name)

	# make database
	if help_db_name not in dbman.get_database_list():
		try:
			dbman.create_user(help_db_name, help_db_name)
		except Exception as e:
			# user already exists
			if e.args[0] != 1396:
				raise
		dbman.create_database(help_db_name)
		dbman.grant_all_privileges(help_db_name, help_db_name)
		dbman.flush_privileges()

=======
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581

<<<<<<< HEAD
def drop_user_and_database(db_name, root_login, root_password):
	frappe.local.db = get_root_connection(root_login, root_password)
=======
def drop_user_and_database(
	db_name,
	db_user,
):
	frappe.local.db = get_root_connection()
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	dbman = DbManager(frappe.local.db)
	dbman.drop_database(db_name)
	dbman.delete_user(db_user, host="%")
	dbman.delete_user(db_user)


def bootstrap_database(verbose, source_sql=None):
	import sys

<<<<<<< HEAD
	frappe.connect(db_name=db_name)
=======
	frappe.connect()
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	check_compatible_versions()

	import_db_from_sql(source_sql, verbose)
	frappe.connect()

<<<<<<< HEAD
=======
	frappe.connect()
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	if "tabDefaultValue" not in frappe.db.get_tables(cached=False):
		from click import secho

		secho(
			"Table 'tabDefaultValue' missing in the restored site. "
			"This happens when the backup fails to restore. Please check that the file is valid\n"
			"Do go through the above output to check the exact error message from MariaDB",
			fg="red",
		)
		sys.exit(1)


def import_db_from_sql(source_sql=None, verbose=False):
	if verbose:
		print("Starting database import...")
	db_name = frappe.conf.db_name
	if not source_sql:
		source_sql = os.path.join(os.path.dirname(__file__), "framework_mariadb.sql")
	DbManager(frappe.local.db).restore_database(
<<<<<<< HEAD
		verbose, db_name, source_sql, db_name, frappe.conf.db_password
	)
	if verbose:
		print("Imported from database %s" % source_sql)
=======
		verbose, db_name, source_sql, frappe.conf.db_user, frappe.conf.db_password
	)
	if verbose:
		print("Imported from database {}".format(source_sql))
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b


def check_compatible_versions():
	try:
		version = get_mariadb_version()
		version_tuple = tuple(int(v) for v in version[0].split("."))

<<<<<<< HEAD
		if version_tuple < (10, 3):
			click.secho(
				f"Warning: MariaDB version {version} is less than 10.3 which is not supported by Frappe",
				fg="yellow",
			)
		elif version_tuple >= (10, 9):
			click.secho(
				f"Warning: MariaDB version {version} is more than 10.8 which is not yet tested with Frappe Framework.",
=======
		if version_tuple < (10, 6):
			click.secho(
				f"Warning: MariaDB version {version} is older than 10.6 which is not supported by Frappe",
				fg="yellow",
			)
		elif version_tuple > (11, 3):
			click.secho(
				f"Warning: MariaDB version {version} is newer than 11.3 which is not yet tested with Frappe Framework.",
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
				fg="yellow",
			)
	except Exception:
		click.secho(
			"MariaDB version compatibility checks failed, make sure you're running a supported version.",
			fg="yellow",
		)

<<<<<<< HEAD

def get_root_connection(root_login, root_password):
	import getpass
=======
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581

def get_root_connection():
	if not frappe.local.flags.root_connection:
		from getpass import getpass

		if not frappe.flags.root_login:
			frappe.flags.root_login = (
				frappe.conf.get("mariadb_root_login")
				or frappe.conf.get("root_login")
				or (sys.__stdin__.isatty() and input("Enter mysql super user [root]: "))
				or "root"
			)

		if not frappe.flags.root_password:
			frappe.flags.root_password = (
				frappe.conf.get("mariadb_root_password")
				or frappe.conf.get("root_password")
				or getpass("MySQL root password: ")
			)

<<<<<<< HEAD
		frappe.local.flags.root_connection = frappe.database.get_db(user=root_login, password=root_password)
=======
		frappe.local.flags.root_connection = frappe.database.get_db(
			socket=frappe.conf.db_socket,
			host=frappe.conf.db_host,
			port=frappe.conf.db_port,
<<<<<<< HEAD
			user=root_login,
			password=root_password,
=======
			user=frappe.flags.root_login,
			password=frappe.flags.root_password,
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
			cur_db_name=None,
		)
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581

	return frappe.local.flags.root_connection
