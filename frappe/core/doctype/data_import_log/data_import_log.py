# Copyright (c) 2021, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DataImportLog(Document):
<<<<<<< HEAD
	no_feed_on_delete = True
=======
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		data_import: DF.Link | None
		docname: DF.Data | None
		exception: DF.Text | None
		log_index: DF.Int
		messages: DF.Code | None
		row_indexes: DF.Code | None
		success: DF.Check
	# end: auto-generated types

	no_feed_on_delete = True

	pass
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
