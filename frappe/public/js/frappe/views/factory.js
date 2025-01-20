// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide("frappe.pages");
frappe.provide("frappe.views");

frappe.views.Factory = class Factory {
	constructor(opts) {
		$.extend(this, opts);
	}

	show() {
		this.route = frappe.get_route();
		this.page_name = frappe.get_route_str();

		if (this.before_show && this.before_show() === false) return;

		if (frappe.pages[this.page_name]) {
			frappe.container.change_to(this.page_name);
			if (this.on_show) {
				this.on_show();
			}
		} else {
			if (this.route[1]) {
				this.make(this.route);
			} else {
				frappe.show_not_found(this.route);
			}
		}
	}

	make_page(double_column, page_name, sidebar_postition) {
		return frappe.make_page(double_column, page_name, sidebar_postition);
	}
};

<<<<<<< HEAD
frappe.make_page = function (double_column, page_name) {
=======
frappe.make_page = function (double_column, page_name, sidebar_position) {
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	if (!page_name) {
		page_name = frappe.get_route_str();
	}

	const page = frappe.container.add_page(page_name);

	frappe.ui.make_app_page({
		parent: page,
		single_column: !double_column,
<<<<<<< HEAD
=======
		sidebar_position: sidebar_position,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
		disable_sidebar_toggle: !sidebar_position,
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	});

	frappe.container.change_to(page_name);
	return page;
};
