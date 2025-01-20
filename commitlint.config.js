module.exports = {
	parserPreset: "conventional-changelog-conventionalcommits",
	rules: {
		"subject-empty": [2, "never"],
		"type-case": [2, "always", "lower-case"],
		"type-empty": [2, "never"],
		"type-enum": [
			2,
			"always",
			[
				"build",
				"chore",
				"ci",
				"docs",
				"feat",
				"fix",
				"perf",
				"refactor",
				"revert",
				"style",
				"test",
<<<<<<< HEAD
=======
				"deprecate", // deprecation decision
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			],
		],
	},
};
