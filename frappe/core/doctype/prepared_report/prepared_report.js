// Copyright (c) 2018, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Prepared Report", {
<<<<<<< HEAD
	render_filter_values: function (frm) {
=======
	render_filter_values: function (frm, filters) {
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
		var wrapper = $(frm.fields_dict["filter_values"].wrapper).empty();

		let filter_table = $(`<table class="table table-bordered">
			<thead>
				<tr>
					<td>${__("Filter")}</td>
					<td>${__("Value")}</td>
				</tr>
			</thead>
			<tbody></tbody>
		</table>`);

<<<<<<< HEAD
		const filters = JSON.parse(frm.doc.filters);
		frm.toggle_display(["filter_values"], !$.isEmptyObject(filters));

=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
		Object.keys(filters).forEach((key) => {
			const filter_row = $(`<tr>
				<td>${frappe.model.unscrub(key)}</td>
				<td>${filters[key]}</td>
			</tr>`);
			filter_table.find("tbody").append(filter_row);
		});

		wrapper.append(filter_table);
	},

	refresh: function (frm) {
		frm.disable_save();
<<<<<<< HEAD
		frm.events.render_filter_values(frm);
=======

		const filters = JSON.parse(frm.doc.filters);
		if (!$.isEmptyObject(filters)) {
			frm.toggle_display(["filter_values"], 1);
			frm.events.render_filter_values(frm, filters);
		}
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02

		// always keep report_name hidden - we do this as we can't set mandatory and hidden
		// property on a docfield at the same time
		frm.toggle_display(["report_name"], 0);

		if (frm.doc.status == "Completed") {
			frm.page.set_primary_action(__("Show Report"), () => {
				frappe.route_options = { prepared_report_name: frm.doc.name };
				frappe.set_route("query-report", frm.doc.report_name);
			});
		}
	},
});
