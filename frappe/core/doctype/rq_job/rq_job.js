// Copyright (c) 2022, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("RQ Job", {
	refresh: function (frm) {
		// Nothing in this form is supposed to be editable.
		frm.disable_form();
		frm.dashboard.set_headline_alert(
<<<<<<< HEAD
			"This is a virtual doctype and data is cleared periodically."
=======
			__("This is a virtual doctype and data is cleared periodically.")
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		);

		if (["started", "queued"].includes(frm.doc.status)) {
			frm.add_custom_button(__("Force Stop job"), () => {
				frappe.confirm(
<<<<<<< HEAD
					"This will terminate the job immediately and might be dangerous, are you sure? ",
=======
					__(
						"This will terminate the job immediately and might be dangerous, are you sure? "
					),
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
					() => {
						frappe
							.xcall("frappe.core.doctype.rq_job.rq_job.stop_job", {
								job_id: frm.doc.name,
							})
							.then((r) => {
<<<<<<< HEAD
								frappe.show_alert("Job Stopped Succefully");
=======
								frappe.show_alert(__("Job Stopped Successfully"));
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
								frm.reload_doc();
							});
					}
				);
			});
		}
	},
});
