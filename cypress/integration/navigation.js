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
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
		cy.go("back");
		cy.title().should("eq", "Website");
	});

<<<<<<< HEAD
	it.only("Navigate to previous page after login", () => {
=======
	it("Navigate to previous page after login", () => {
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
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
