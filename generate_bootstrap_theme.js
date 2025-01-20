const sass = require("sass");
const fs = require("fs");
const sass_options = require("./esbuild/sass_options");
let output_path = process.argv[2];
let scss_content = process.argv[3];
scss_content = scss_content.replace(/\\n/g, "\n");

sass.render(
	{
		data: scss_content,
		outputStyle: "compressed",
		...sass_options,
	},
	function (err, result) {
		if (err) {
<<<<<<< HEAD
			console.error(err.formatted); // eslint-disable-line
=======
			console.error(err.formatted);
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			return;
		}

		fs.writeFile(output_path, result.css, function (err) {
			if (!err) {
<<<<<<< HEAD
				console.log(output_path); // eslint-disable-line
			} else {
				console.error(err); // eslint-disable-line
=======
				console.log(output_path);
			} else {
				console.error(err);
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			}
		});
	}
);
