const { defineConfig } = require("cypress");
<<<<<<< HEAD
=======
const fs = require("fs");
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b

module.exports = defineConfig({
	projectId: "92odwv",
	adminPassword: "admin",
	testUser: "frappe@example.com",
	defaultCommandTimeout: 20000,
	pageLoadTimeout: 15000,
	video: true,
<<<<<<< HEAD
	videoUploadOnPasses: false,
	viewportWidth: 1920,
	viewportHeight: 1200,
=======
	viewportHeight: 960,
	viewportWidth: 1400,
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	retries: {
		runMode: 1,
		openMode: 1,
	},
	e2e: {
		// We've imported your old cypress plugins here.
		// You may want to clean this up later by importing these.
		setupNodeEvents(on, config) {
<<<<<<< HEAD
=======
			// Delete videos for specs without failing or retried tests
			// https://docs.cypress.io/guides/guides/screenshots-and-videos#Delete-videos-for-specs-without-failing-or-retried-tests
			on("after:spec", (spec, results) => {
				if (results && results.video) {
					const failures = results.tests.some((test) =>
						test.attempts.some((attempt) => attempt.state === "failed")
					);
					if (!failures) {
						fs.unlinkSync(results.video);
					}
				}
			});

>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
			return require("./cypress/plugins/index.js")(on, config);
		},
		testIsolation: false,
		baseUrl: "http://test_site_ui:8000",
		specPattern: ["./cypress/integration/*.js", "**/ui_test_*.js"],
	},
});
