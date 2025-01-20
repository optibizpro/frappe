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
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
