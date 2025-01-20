frappe.listview_settings["Contact"] = {
	add_fields: ["image"],
<<<<<<< HEAD
=======
	onload: function (listview) {
		listview.page.add_action_item(__("Download vCards"), function () {
			const contacts = listview.get_checked_items();
			open_url_post("/api/method/frappe.contacts.doctype.contact.contact.download_vcards", {
				contacts: contacts.map((c) => c.name),
			});
		});
	},
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
};
