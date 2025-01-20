frappe.listview_settings["Note"] = {
<<<<<<< HEAD
	onload: function (me) {
		me.page.set_title(__("Notes"));
	},
	add_fields: ["title", "public"],
=======
	hide_name_column: true,
	add_fields: ["public"],
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
	get_indicator: function (doc) {
		if (doc.public) {
			return [__("Public"), "green", "public,=,Yes"];
		} else {
			return [__("Private"), "gray", "public,=,No"];
		}
	},
};
