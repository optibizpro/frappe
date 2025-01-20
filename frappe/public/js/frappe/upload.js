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
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
