frappe.listview_settings["Error Log"] = {
	add_fields: ["seen"],
	get_indicator: function (doc) {
		if (cint(doc.seen)) {
			return [__("Seen"), "green", "seen,=,1"];
		} else {
			return [__("Not Seen"), "red", "seen,=,0"];
		}
	},
<<<<<<< HEAD
	order_by: "seen asc, modified desc",
=======
	order_by: "creation desc",
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	onload: function (listview) {
		listview.page.add_menu_item(__("Clear Error Logs"), function () {
			frappe.call({
				method: "frappe.core.doctype.error_log.error_log.clear_error_logs",
				callback: function () {
					listview.refresh();
				},
			});
		});

		frappe.require("logtypes.bundle.js", () => {
			frappe.utils.logtypes.show_log_retention_message(cur_list.doctype);
		});
	},
};
