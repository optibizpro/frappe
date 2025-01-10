frappe.listview_settings["Workflow Action"] = {
	get_form_link: (doc) => {
		let doctype = "";
		let docname = "";
		if (doc.status === "Open") {
			doctype = doc.reference_doctype;
			docname = doc.reference_name;
		} else {
			doctype = "Workflow Action";
			docname = doc.name;
		}
		docname = docname.match(/[%'"]/) ? encodeURIComponent(docname) : docname;

<<<<<<< HEAD
		const link = "/app/" + frappe.router.slug(doctype) + "/" + docname;
		return link;
=======
		return "/app/" + frappe.router.slug(doctype) + "/" + docname;
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	},
};
