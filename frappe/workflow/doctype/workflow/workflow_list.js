frappe.listview_settings["Workflow"] = {
	add_fields: ["is_active"],
	get_indicator: function (doc) {
		if (doc.is_active) {
			return [__("Active"), "green", "is_active,=,Yes"];
		} else if (!doc.is_active) {
			return [__("Not active"), "gray", "is_active,=,No"];
		}
	},
<<<<<<< HEAD
=======
	button: {
		show(doc) {
			return doc.name;
		},
		get_label() {
			return frappe.utils.icon("workflow", "sm");
		},
		get_description(doc) {
			return __("Build {0}", [`${doc.name}`]);
		},
		action(doc) {
			frappe.set_route("workflow-builder", doc.name);
		},
	},
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
};

frappe.help.youtube_id["Workflow"] = "yObJUg9FxFs";
