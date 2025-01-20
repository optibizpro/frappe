// Copyright (c) 2018, Frappe Technologies and contributors
// For license information, please see license.txt

const DATE_BASED_EVENTS = ["Days Before", "Days After"];

frappe.notification = {
	setup_fieldname_select: function (frm) {
		// get the doctype to update fields
		if (!frm.doc.document_type) {
			return;
		}

		frappe.model.with_doctype(frm.doc.document_type, function () {
			let get_select_options = function (df, parent_field) {
				// Append parent_field name along with fieldname for child table fields
				let select_value = parent_field ? df.fieldname + "," + parent_field : df.fieldname;
<<<<<<< HEAD

				return {
					value: select_value,
					label: df.fieldname + " (" + __(df.label) + ")",
				};
			};

			let get_date_change_options = function () {
				let date_options = $.map(fields, function (d) {
					return d.fieldtype == "Date" || d.fieldtype == "Datetime"
						? get_select_options(d)
						: null;
=======
				let path = parent_field ? parent_field + " > " + df.fieldname : df.fieldname;

				return {
					value: select_value,
<<<<<<< HEAD
					label: df.fieldname + " (" + __(df.label, null, df.parent) + ")",
=======
					label: path + " (" + __(df.label, null, df.parent) + ")",
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
				};
			};

			let get_date_change_options = function (fieldtypes) {
				let date_options = $.map(fields, function (d) {
					return fieldtypes.includes(d.fieldtype) ? get_select_options(d) : null;
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
				});
				// append creation and modified date to Date Change field
				return date_options.concat([
					{ value: "creation", label: `creation (${__("Created On")})` },
					{ value: "modified", label: `modified (${__("Last Modified Date")})` },
				]);
			};
			let get_receiver_fields = function (
				fields,
				is_extra_receiver_field = (_) => {
					return false;
				}
			) {
				// finds receiver fields from the fields or any child table
				// by default finds any link to the User doctype
				// however an additional optional predicate can be passed as argument
				// to find additional fields
				let is_receiver_field = function (df) {
					return (
						is_extra_receiver_field(df) ||
						(df.options == "User" && df.fieldtype == "Link") ||
						(df.options == "Customer" && df.fieldtype == "Link")
					);
				};
				let extract_receiver_field = function (df) {
					// Add recipients from child doctypes into select dropdown
					if (frappe.model.table_fields.includes(df.fieldtype)) {
						let child_fields = frappe.get_doc("DocType", df.options).fields;
						return $.map(child_fields, function (cdf) {
							return is_receiver_field(cdf)
								? get_select_options(cdf, df.fieldname)
								: null;
						});
					} else {
						return is_receiver_field(df) ? get_select_options(df) : null;
					}
				};
				return $.map(fields, extract_receiver_field);
			};

			let fields = frappe.get_doc("DocType", frm.doc.document_type).fields;
			let options = $.map(fields, function (d) {
<<<<<<< HEAD
				return in_list(frappe.model.no_value_type, d.fieldtype)
=======
				return frappe.model.no_value_type.includes(d.fieldtype)
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
					? null
					: get_select_options(d);
			});

			// set value changed options
			frm.set_df_property("value_changed", "options", [""].concat(options));
			frm.set_df_property("set_property_after_alert", "options", [""].concat(options));

			// set date changed options
<<<<<<< HEAD
			frm.set_df_property("date_changed", "options", get_date_change_options());

			let receiver_fields = [];
			if (frm.doc.channel === "Email") {
				receiver_fields = $.map(fields, function (d) {
					// Add User and Email fields from child into select dropdown
					if (frappe.model.table_fields.includes(d.fieldtype)) {
						let child_fields = frappe.get_doc("DocType", d.options).fields;
						return $.map(child_fields, function (df) {
							return df.options == "Email" ||
								(df.options == "User" && df.fieldtype == "Link")
								? get_select_options(df, d.fieldname)
								: null;
						});
						// Add User and Email fields from parent into select dropdown
					} else {
						return d.options == "Email" ||
							(d.options == "User" && d.fieldtype == "Link")
							? get_select_options(d)
							: null;
					}
				});
			} else if (in_list(["WhatsApp", "SMS"], frm.doc.channel)) {
				receiver_fields = $.map(fields, function (d) {
					return d.options == "Phone" ? get_select_options(d) : null;
=======
			frm.set_df_property(
				"date_changed",
				"options",
				get_date_change_options(["Date", "Datetime"])
			);
			frm.set_df_property(
				"datetime_changed",
				"options",
				get_date_change_options(["Datetime"])
			);

			let receiver_fields = [];
			if (frm.doc.channel === "Email") {
				receiver_fields = get_receiver_fields(fields, function (df) {
					return df.options == "Email";
				});
			} else if (["WhatsApp", "SMS"].includes(frm.doc.channel)) {
<<<<<<< HEAD
				receiver_fields = $.map(fields, function (d) {
					return d.options == "Phone" ? get_select_options(d) : null;
=======
				receiver_fields = get_receiver_fields(fields, function (df) {
					df.options == "Phone" || df.options == "Mobile";
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
				});
			}

			// set email recipient options
			frm.fields_dict.recipients.grid.update_docfield_property(
				"receiver_by_document_field",
				"options",
				[""].concat(["owner"]).concat(receiver_fields)
			);
		});
	},
	setup_example_message: function (frm) {
		let template = "";
		if (frm.doc.channel === "Email") {
			template = `<h5>Message Example</h5>

<pre>&lt;h3&gt;Order Overdue&lt;/h3&gt;

&lt;p&gt;Transaction {{ doc.name }} has exceeded Due Date. Please take necessary action.&lt;/p&gt;

&lt;!-- show last comment --&gt;
{% if comments %}
Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}
{% endif %}

&lt;h4&gt;Details&lt;/h4&gt;

&lt;ul&gt;
&lt;li&gt;Customer: {{ doc.customer }}&lt;/li&gt;
&lt;li&gt;Amount: {{ doc.grand_total }}&lt;/li&gt;
&lt;/ul&gt;
</pre>
			`;
<<<<<<< HEAD
		} else if (in_list(["Slack", "System Notification", "SMS"], frm.doc.channel)) {
=======
		} else if (["Slack", "System Notification", "SMS"].includes(frm.doc.channel)) {
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
			template = `<h5>Message Example</h5>

<pre>*Order Overdue*

Transaction {{ doc.name }} has exceeded Due Date. Please take necessary action.

<!-- show last comment -->
{% if comments %}
Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}
{% endif %}

*Details*

• Customer: {{ doc.customer }}
• Amount: {{ doc.grand_total }}
</pre>`;
		}
		if (template) {
			frm.set_df_property("message_examples", "options", template);
		}
	},
};

frappe.ui.form.on("Notification", {
	onload: function (frm) {
		frm.set_query("document_type", function () {
			if (DATE_BASED_EVENTS.includes(frm.doc.event)) return;

			return {
				filters: {
					istable: 0,
				},
			};
		});
		frm.set_query("print_format", function () {
			return {
				filters: {
					doc_type: frm.doc.document_type,
				},
			};
		});
	},
	refresh: function (frm) {
		frappe.notification.setup_fieldname_select(frm);
		frappe.notification.setup_example_message(frm);

		frm.add_fetch("sender", "email_id", "sender_email");
		frm.set_query("sender", () => {
			return {
				filters: {
					enable_outgoing: 1,
				},
			};
		});
		frm.get_field("is_standard").toggle(frappe.boot.developer_mode);
		frm.trigger("event");
<<<<<<< HEAD
	},
	document_type: function (frm) {
		frappe.notification.setup_fieldname_select(frm);
	},
	view_properties: function (frm) {
		frappe.route_options = { doc_type: frm.doc.document_type };
		frappe.set_route("Form", "Customize Form");
	},
	event: function (frm) {
		if (!DATE_BASED_EVENTS.includes(frm.doc.event) || frm.is_new()) return;

		frm.add_custom_button(__("Get Alerts for Today"), function () {
			frappe.call({
				method: "frappe.email.doctype.notification.notification.get_documents_for_today",
				args: {
					notification: frm.doc.name,
				},
				callback: function (r) {
					if (r.message && r.message.length > 0) {
						frappe.msgprint(r.message.toString());
					} else {
						frappe.msgprint(__("No alerts for today"));
					}
				},
=======
		if (frm.doc.document_type) {
			frm.add_custom_button(__("Preview"), () => {
				const args = {
					doc: frm.doc,
					doctype: frm.doc.document_type,
					preview_fields: [
						{
							label: __("Meets Condition?"),
							fieldtype: "Data",
							method: "preview_meets_condition",
						},
						{ label: __("Subject"), fieldtype: "Data", method: "preview_subject" },
						{ label: __("Message"), fieldtype: "Code", method: "preview_message" },
					],
				};
				let dialog = new frappe.views.RenderPreviewer(args);
				return dialog;
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
			});
		});
	},
<<<<<<< HEAD
=======
	document_type: function (frm) {
		frappe.notification.setup_fieldname_select(frm);
	},
	view_properties: function (frm) {
		frappe.route_options = { doc_type: frm.doc.document_type };
		frappe.set_route("Form", "Customize Form");
	},
	event: function (frm) {
		if (!DATE_BASED_EVENTS.includes(frm.doc.event) || frm.is_new()) return;

		frm.add_custom_button(__("Get Alerts for Today"), function () {
			frappe.call({
				method: "frappe.email.doctype.notification.notification.get_documents_for_today",
				args: {
					notification: frm.doc.name,
				},
				callback: function (r) {
					if (r.message && r.message.length > 0) {
						frappe.msgprint(r.message.toString());
					} else {
						frappe.msgprint(__("No alerts for today"));
					}
				},
			});
		});
	},
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
	channel: function (frm) {
		frm.toggle_reqd("recipients", frm.doc.channel == "Email");
		frappe.notification.setup_fieldname_select(frm);
		frappe.notification.setup_example_message(frm);
		if (frm.doc.channel === "SMS" && frm.doc.__islocal) {
			frm.set_df_property(
				"channel",
				"description",
				`To use SMS Channel, initialize <a href="/app/sms-settings">SMS Settings</a>.`
			);
		} else {
			frm.set_df_property("channel", "description", ` `);
		}
	},
});
