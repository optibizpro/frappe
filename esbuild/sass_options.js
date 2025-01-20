let path = require("path");
let { apps_path, app_list } = require("./utils");

<<<<<<< HEAD
let node_modules_path = path.resolve(get_app_path("frappe"), "..", "node_modules");
let app_paths = app_list.map(get_app_path).map((app_path) => path.resolve(app_path, ".."));
=======
let app_paths = app_list.map((app) => path.resolve(apps_path, app));
let node_modules_path = app_paths.map((app_path) => path.resolve(app_path, "node_modules"));
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df

module.exports = {
	includePaths: [...node_modules_path, ...app_paths],
	quietDeps: true,
	importer: function (url) {
		if (url.startsWith("~")) {
			// strip ~ so that it can resolve from node_modules
			url = url.slice(1);
		}
		if (url.endsWith(".css")) {
			// strip .css from end of path
			url = url.slice(0, -4);
		}
		// normal file, let it go
		return {
			file: url,
		};
	},
};
