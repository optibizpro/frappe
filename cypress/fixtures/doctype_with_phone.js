export default {
	name: "Doctype With Phone",
	actions: [],
	custom: 1,
	is_submittable: 1,
	autoname: "field:title",
	creation: "2022-03-30 06:29:07.215072",
	doctype: "DocType",
	engine: "InnoDB",
	fields: [
		{
			fieldname: "title",
			fieldtype: "Data",
			label: "title",
			unique: 1,
		},
		{
			fieldname: "phone",
			fieldtype: "Phone",
			label: "Phone",
		},
	],
	links: [],
	modified: "2019-03-30 14:40:53.127615",
	modified_by: "Administrator",
	naming_rule: "By fieldname",
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
