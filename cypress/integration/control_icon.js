context("Control Icon", () => {
	before(() => {
		cy.login();
		cy.visit("/app/website");
	});

	function get_dialog_with_icon() {
		return cy.dialog({
			title: "Icon",
			fields: [
				{
					label: "Icon",
					fieldname: "icon",
					fieldtype: "Icon",
				},
			],
		});
	}

	it("should set icon", () => {
		get_dialog_with_icon().as("dialog");
		cy.get(".frappe-control[data-fieldname=icon]").findByRole("textbox").click();

		cy.get(".icon-picker .icon-wrapper[id=heart-active]").first().click();
		cy.get(".frappe-control[data-fieldname=icon]")
			.findByRole("textbox")
			.should("have.value", "heart-active");
		cy.get("@dialog").then((dialog) => {
			let value = dialog.get_value("icon");
			expect(value).to.equal("heart-active");
		});

		cy.get(".icon-picker .icon-wrapper[id=heart]").first().click();
		cy.get(".frappe-control[data-fieldname=icon]")
			.findByRole("textbox")
			.should("have.value", "heart");
		cy.get("@dialog").then((dialog) => {
			let value = dialog.get_value("icon");
			expect(value).to.equal("heart");
		});
	});

	it("search for icon and clear search input", () => {
		let search_text = "ed";
<<<<<<< HEAD
		cy.get(".icon-picker").findByRole("searchbox").click().type(search_text);
=======
		cy.get(".icon-picker").get(".search-icons > input").click().type(search_text);
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		cy.get(".icon-section .icon-wrapper:not(.hidden)").then((i) => {
			cy.get(`.icon-section .icon-wrapper[id*='${search_text}']`).then((icons) => {
				expect(i.length).to.equal(icons.length);
			});
		});

<<<<<<< HEAD
		cy.get(".icon-picker").findByRole("searchbox").clear().blur();
=======
		cy.get(".icon-picker").get(".search-icons > input").clear().blur();
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		cy.get(".icon-section .icon-wrapper").should("not.have.class", "hidden");
	});
});
