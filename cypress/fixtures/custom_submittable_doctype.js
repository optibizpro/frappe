export default {
	name: "Custom Submittable DocType",
	custom: 1,
	actions: [],
	is_submittable: 1,
	creation: "2019-12-10 06:29:07.215072",
	doctype: "DocType",
	editable_grid: 1,
	engine: "InnoDB",
	fields: [
		{
			fieldname: "enabled",
			fieldtype: "Check",
			label: "Enabled",
			allow_on_submit: 1,
			reqd: 1,
		},
		{
			fieldname: "title",
			fieldtype: "Data",
			label: "title",
			reqd: 1,
		},
		{
			fieldname: "description",
			fieldtype: "Text Editor",
			label: "Description",
		},
	],
	links: [],
	modified: "2019-12-10 14:40:53.127615",
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
			submit: 1,
			cancel: 1,
		},
	],
	quick_entry: 1,
<<<<<<< HEAD
	sort_field: "modified",
=======
	sort_field: "creation",
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
	sort_order: "ASC",
	track_changes: 1,
};
