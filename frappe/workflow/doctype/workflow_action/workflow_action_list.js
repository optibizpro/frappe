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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	},
};
