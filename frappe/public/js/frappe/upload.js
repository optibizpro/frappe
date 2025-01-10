// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

<<<<<<< HEAD
import FileUploader from "./file_uploader";

frappe.provide("frappe.ui");
frappe.ui.FileUploader = FileUploader;
=======
if (frappe.require) {
	frappe.require("file_uploader.bundle.js");
} else {
	frappe.ready(function () {
		frappe.require("file_uploader.bundle.js");
	});
}
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
