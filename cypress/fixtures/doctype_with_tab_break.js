export default {
	name: "Form With Tab Break",
	custom: 1,
	actions: [],
	doctype: "DocType",
	engine: "InnoDB",
	fields: [
		{
			fieldname: "username",
			fieldtype: "Data",
			label: "Name",
			options: "Name",
		},
		{
			fieldname: "tab",
			fieldtype: "Tab Break",
			label: "Tab 2",
		},
		{
			fieldname: "Phone",
			fieldtype: "Data",
			label: "Phone",
			options: "Phone",
			reqd: 1,
		},
	],
	links: [
		{
			group: "Profile",
			link_doctype: "Contact",
			link_fieldname: "user",
		},
	],
	modified_by: "Administrator",
	module: "Custom",
	owner: "Administrator",
	permissions: [
		{
			create: 1,
			delete: 1,
			email: 1,
			print: 1,
			read: 1,
			role: "System Manager",
			share: 1,
			write: 1,
		},
	],
	quick_entry: 1,
	autoname: "format: Test-{####}",
<<<<<<< HEAD
	sort_field: "modified",
=======
	sort_field: "creation",
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	sort_order: "ASC",
	track_changes: 1,
};
