export default {
	name: "Doctype With Child Table",
	actions: [],
	custom: 1,
	autoname: "field:title",
	creation: "2022-02-09 20:15:21.242213",
	doctype: "DocType",
	editable_grid: 1,
	engine: "InnoDB",
	fields: [
		{
			fieldname: "title",
			fieldtype: "Data",
			label: "Title",
			unique: 1,
		},
		{
			fieldname: "child_table",
			fieldtype: "Table",
			label: "Child Table",
			options: "Child Table Doctype",
			reqd: 1,
		},
		{
			fieldname: "child_table_1",
			fieldtype: "Table",
			label: "Child Table 1",
			options: "Child Table Doctype 1",
		},
	],
	links: [],
	modified: "2022-02-10 12:03:12.603763",
	modified_by: "Administrator",
	module: "Custom",
	naming_rule: "By fieldname",
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
