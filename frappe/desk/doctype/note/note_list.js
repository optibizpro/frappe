frappe.listview_settings["Note"] = {
<<<<<<< HEAD
	onload: function (me) {
		me.page.set_title(__("Notes"));
	},
	add_fields: ["title", "public"],
=======
	hide_name_column: true,
	add_fields: ["public"],
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	get_indicator: function (doc) {
		if (doc.public) {
			return [__("Public"), "green", "public,=,Yes"];
		} else {
			return [__("Private"), "gray", "public,=,No"];
		}
	},
};
