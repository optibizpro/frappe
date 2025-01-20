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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
			}
		});
	}
);
