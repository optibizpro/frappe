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
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
