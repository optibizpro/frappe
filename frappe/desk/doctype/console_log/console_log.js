// Copyright (c) 2020, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Console Log", {
<<<<<<< HEAD
	// refresh: function(frm) {
	// }
=======
	refresh: function (frm) {
		frm.add_custom_button(__("Re-Run in Console"), () => {
			window.localStorage.setItem("system_console_code", frm.doc.script);
			window.localStorage.setItem("system_console_type", frm.doc.type);
			frappe.set_route("Form", "System Console");
		});
	},
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
});
