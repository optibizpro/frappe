context("Navigation", () => {
	before(() => {
		cy.visit("/login");
		cy.login();
		cy.visit("/app/website");
	});
	it("Navigate to route with hash in document name", () => {
<<<<<<< HEAD
		cy.insert_doc("ToDo", {
			__newname: "ABC#123",
			description: "Test this",
			ignore_duplicate: true,
		});
		cy.visit("/app/todo/ABC#123");
		cy.title().should("eq", "Test this - ABC#123");
		cy.get_field("description", "Text Editor").contains("Test this");
=======
		cy.insert_doc(
			"Client Script",
			{
				__newname: "ABC#123",
				dt: "User",
				script: "console.log('ran')",
				enabled: 0,
			},
			true
		);
		cy.visit(`/app/client-script/${encodeURIComponent("ABC#123")}`);
		cy.title().should("eq", "ABC#123");
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		cy.go("back");
		cy.title().should("eq", "Website");
	});

<<<<<<< HEAD
	it.only("Navigate to previous page after login", () => {
=======
	it("Navigate to previous page after login", () => {
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		cy.visit("/app/todo");
		cy.get(".page-head").findByTitle("To Do").should("be.visible");
		cy.clear_filters();
		cy.call("logout");
		cy.reload().as("reload");
		cy.get("@reload").get(".page-card .btn-primary").contains("Login").click();
		cy.location("pathname").should("eq", "/login");
		cy.login();
		cy.reload().as("reload");
		cy.location("pathname").should("eq", "/app/todo");
	});
});
