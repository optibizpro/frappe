// Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

// Common utility functions for logging doctypes.

frappe.provide("frappe.utils.logtypes");

frappe.utils.logtypes.show_log_retention_message = (doctype) => {
	if (!frappe.model.can_write("Log Settings")) {
		return;
	}

	const add_sidebar_message = (message) => {
<<<<<<< HEAD
		let sidebar_entry = $('<ul class="list-unstyled sidebar-menu"></ul>').appendTo(
=======
		let sidebar_entry = $('<div class="sidebar-section></div>').appendTo(
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
			cur_list.page.sidebar
		);
		$(`<div>${message}</div>`).appendTo(sidebar_entry);
	};

	const log_settings_link = `<a href='/app/log-settings'>${__("Log Settings")}</a>`;
	const cta = __("You can change the retention policy from {0}.", [log_settings_link]);
	let message = __("{0} records are not automatically deleted.", [__(doctype)]);

	frappe.db
		.get_value("Logs To Clear", { ref_doctype: doctype }, "days", null, "Log Settings")
		.then((r) => {
			if (!r.exc && r.message && r.message.days) {
				message = __("{0} records are retained for {1} days.", [
					__(doctype),
					r.message.days,
				]);
			}
			add_sidebar_message(`${message} ${cta}`);
		});
};
