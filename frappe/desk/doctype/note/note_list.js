frappe.listview_settings["Note"] = {
<<<<<<< HEAD
	onload: function (me) {
		me.page.set_title(__("Notes"));
	},
	add_fields: ["title", "public"],
=======
	hide_name_column: true,
	add_fields: ["public"],
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	get_indicator: function (doc) {
		if (doc.public) {
			return [__("Public"), "green", "public,=,Yes"];
		} else {
			return [__("Private"), "gray", "public,=,No"];
		}
	},
};
