<<<<<<< HEAD
""" Utils for thread/process synchronization. """
=======
"""Utils for thread/process synchronization."""
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

import os
from contextlib import contextmanager

from filelock import FileLock as _StrongFileLock
from filelock import Timeout

import frappe
from frappe import _
from frappe.utils import get_bench_path, get_site_path
from frappe.utils.file_lock import LockTimeoutError

LOCKS_DIR = "locks"


@contextmanager
def filelock(lock_name: str, *, timeout=30, is_global=False):
	"""Create a lockfile to prevent concurrent operations acrosss processes.

	args:
	        lock_name: Unique name to identify a specific lock. Lockfile called `{name}.lock` will be
	        created.
	        timeout: time to wait before failing.
	        is_global: if set lock is global to bench

	Lock file location:
	        global - {bench_dir}/config/{name}.lock
	        site - {bench_dir}/sites/sitename/{name}.lock

	"""

	lock_filename = lock_name + ".lock"
	if not is_global:
		lock_path = os.path.abspath(get_site_path(LOCKS_DIR, lock_filename))
	else:
		lock_path = os.path.abspath(os.path.join(get_bench_path(), "config", lock_filename))

	try:
		with _StrongFileLock(lock_path, timeout=timeout):
			yield
	except Timeout as e:
<<<<<<< HEAD
		frappe.log_error("Filelock: Failed to aquire {lock_path}")

		raise LockTimeoutError(
			_("Failed to aquire lock: {}").format(lock_name)
=======
		frappe.log_error(f"Filelock: Failed to aquire {lock_path}")

		raise LockTimeoutError(
			_("Failed to aquire lock: {}. Lock may be held by another process.").format(lock_name)
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
			+ "<br>"
			+ _("You can manually remove the lock if you think it's safe: {}").format(lock_path)
		) from e
