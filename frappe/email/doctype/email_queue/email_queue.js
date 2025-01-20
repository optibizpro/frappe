// Copyright (c) 2016, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Email Queue", {
	refresh: function (frm) {
		if (["Not Sent", "Partially Sent"].includes(frm.doc.status)) {
			let button = frm.add_custom_button("Send Now", function () {
				frappe.call({
					method: "frappe.email.doctype.email_queue.email_queue.send_now",
					args: {
						name: frm.doc.name,
					},
					btn: button,
					callback: function () {
						frm.reload_doc();
						if (cint(frappe.sys_defaults.suspend_email_queue)) {
							frappe.show_alert(
								__(
									"Email queue is currently suspended. Resume to automatically send emails."
								)
							);
						}
					},
				});
			});
		} else if (frm.doc.status == "Error") {
<<<<<<< HEAD
			frm.add_custom_button(__("Retry Sending"), function () {
				frm.call({
					method: "retry_sending",
					doc: frm.doc,
					args: {
						name: frm.doc.name,
					},
					callback: function () {
						frm.reload_doc();
=======
			frm.add_custom_button("Retry Sending", function () {
				frm.call({
					method: "frappe.email.doctype.email_queue.email_queue.retry_sending",
					args: {
						queues: [frm.doc.name],
					},
					callback: function () {
						frm.reload_doc();
						frappe.show_alert({
							message: __(
								"Status Updated. The email will be picked up in the next scheduled run."
							),
							indicator: "green",
						});
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
					},
				});
			});
		}
	},
});
