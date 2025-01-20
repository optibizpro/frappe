# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

# Database Module
# --------------------
from shutil import which

from frappe.database.database import savepoint


def setup_database(force, verbose=None, mariadb_user_host_login_scope=None):
	import frappe

	if frappe.conf.db_type == "postgres":
		import frappe.database.postgres.setup_db

		return frappe.database.postgres.setup_db.setup_database()
	else:
		import frappe.database.mariadb.setup_db

		return frappe.database.mariadb.setup_db.setup_database(force, verbose, mariadb_user_host_login_scope)
<<<<<<< HEAD


def bootstrap_database(verbose=None, source_sql=None):
	import frappe

	if frappe.conf.db_type == "postgres":
		import frappe.database.postgres.setup_db

<<<<<<< HEAD
		return frappe.database.postgres.setup_db.drop_user_and_database(db_name, root_login, root_password)
	else:
		import frappe.database.mariadb.setup_db

		return frappe.database.mariadb.setup_db.drop_user_and_database(db_name, root_login, root_password)


def get_db(host=None, user=None, password=None, port=None):
=======
<<<<<<< HEAD
		return frappe.database.postgres.setup_db.bootstrap_database(verbose, source_sql)
	else:
		import frappe.database.mariadb.setup_db

		return frappe.database.mariadb.setup_db.bootstrap_database(verbose, source_sql)
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b


def bootstrap_database(verbose=None, source_sql=None):
	import frappe

	if frappe.conf.db_type == "postgres":
		import frappe.database.postgres.setup_db

<<<<<<< HEAD
		return frappe.database.postgres.setup_db.drop_user_and_database(db_name, root_login, root_password)
	else:
		import frappe.database.mariadb.setup_db

		return frappe.database.mariadb.setup_db.drop_user_and_database(db_name, root_login, root_password)


def get_db(host=None, user=None, password=None, port=None, cur_db_name=None, socket=None):
=======
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		return frappe.database.postgres.setup_db.bootstrap_database(verbose, source_sql)
	else:
		import frappe.database.mariadb.setup_db

		return frappe.database.mariadb.setup_db.bootstrap_database(verbose, source_sql)


def drop_user_and_database(db_name, db_user):
	import frappe

	if frappe.conf.db_type == "postgres":
		import frappe.database.postgres.setup_db

		return frappe.database.postgres.setup_db.drop_user_and_database(db_name, db_user)
	else:
		import frappe.database.mariadb.setup_db

		return frappe.database.mariadb.setup_db.drop_user_and_database(db_name, db_user)


def get_db(socket=None, host=None, user=None, password=None, port=None, cur_db_name=None):
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
	import frappe

	if frappe.conf.db_type == "postgres":
		import frappe.database.postgres.database

<<<<<<< HEAD
		return frappe.database.postgres.database.PostgresDatabase(host, user, password, port=port)
	else:
		import frappe.database.mariadb.database

		return frappe.database.mariadb.database.MariaDBDatabase(host, user, password, port=port)
=======
		return frappe.database.postgres.database.PostgresDatabase(
<<<<<<< HEAD
			host, user, password, port, cur_db_name, socket
=======
			socket, host, user, password, port, cur_db_name
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		)
	else:
		import frappe.database.mariadb.database

		return frappe.database.mariadb.database.MariaDBDatabase(
<<<<<<< HEAD
			host, user, password, port, cur_db_name, socket
=======
			socket, host, user, password, port, cur_db_name
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
		)
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df


def get_command(
<<<<<<< HEAD
	host=None, port=None, user=None, password=None, db_name=None, extra=None, dump=False, socket=None
=======
	socket=None, host=None, port=None, user=None, password=None, db_name=None, extra=None, dump=False
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
):
	import frappe

	if frappe.conf.db_type == "postgres":
		if dump:
			bin, bin_name = which("pg_dump"), "pg_dump"
		else:
			bin, bin_name = which("psql"), "psql"

		if socket and password:
			conn_string = f"postgresql://{user}:{password}@/{db_name}?host={socket}"
		elif socket:
			conn_string = f"postgresql://{user}@/{db_name}?host={socket}"
		elif password:
			conn_string = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
		else:
			conn_string = f"postgresql://{user}@{host}:{port}/{db_name}"

		command = [conn_string]

		if extra:
			command.extend(extra)

	else:
		if dump:
			bin, bin_name = which("mariadb-dump") or which("mysqldump"), "mariadb-dump"
		else:
			bin, bin_name = which("mariadb") or which("mysql"), "mariadb"

		command = [f"--user={user}"]
		if socket:
			command.append(f"--socket={socket}")
		elif host and port:
			command.append(f"--host={host}")
			command.append(f"--port={port}")

		if password:
			command.append(f"--password={password}")

		if dump:
			command.extend(
				[
					"--single-transaction",
					"--quick",
					"--lock-tables=false",
				]
			)
		else:
			command.extend(
				[
					"--pager=less -SFX",
					"--safe-updates",
					"--no-auto-rehash",
				]
			)

		command.append(db_name)

		if extra:
			command.extend(extra)

	return bin, command, bin_name
