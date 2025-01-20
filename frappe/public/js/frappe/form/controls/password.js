frappe.ui.form.ControlPassword = class ControlPassword extends frappe.ui.form.ControlData {
	static input_type = "password";
	make() {
		super.make();
		this.enable_password_checks = true;
	}
	make_input() {
		var me = this;
		super.make_input();
<<<<<<< HEAD
		this.$input
			.parent()
			.append($('<span class="password-strength-indicator indicator"></span>'));
		this.$wrapper
			.find(".control-input-wrapper")
			.append($('<p class="password-strength-message text-muted small hidden"></p>'));

		this.indicator = this.$wrapper.find(".password-strength-indicator");
		this.message = this.$wrapper.find(".help-box");

		this.$input.on("keyup", () => {
			clearTimeout(this.check_password_timeout);
			this.check_password_timeout = setTimeout(() => {
=======

		this.indicator = $(
			`<div class="password-strength-indicator hidden">
				<div class="progress-text"></div>
				<div class="progress">
					<div class="progress-bar" role="progressbar"
						aria-valuenow="0"
						aria-valuemin="0" aria-valuemax="100">
					</div>
				</div>
			</div>`
		).insertAfter(this.$input);

		this.progress_text = this.indicator.find(".progress-text");
		this.progress_bar = this.indicator.find(".progress-bar");
		this.message = this.$wrapper.find(".help-box");

		this.$input.on(
			"keyup",
			frappe.utils.debounce(() => {
				let hide_icon = me.$input.val() && !me.$input.val().includes("*");
				me.toggle_password.toggleClass("hidden", !hide_icon);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
				me.get_password_strength(me.$input.val());
			}, 500)
		);

		this.toggle_password = $(`
			<div class="toggle-password hidden">
				${frappe.utils.icon("unhide", "sm")}
			</div>
		`).insertAfter(this.$input);

		this.toggle_password.on("click", () => {
			if (this.$input.attr("type") === "password") {
				this.$input.attr("type", "text");
				this.toggle_password.html(frappe.utils.icon("hide", "sm"));
			} else {
				this.$input.attr("type", "password");
				this.toggle_password.html(frappe.utils.icon("unhide", "sm"));
			}
		});

		!this.value && this.toggle_password.removeClass("hidden");
	}

	disable_password_checks() {
		this.enable_password_checks = false;
	}

	get_password_strength(value) {
		if (!this.enable_password_checks) {
			return;
		}
<<<<<<< HEAD
=======

		if (!value) {
			this.indicator.addClass("hidden");
			this.message.addClass("hidden");
			return;
		}

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
		var me = this;
		frappe.call({
			type: "POST",
			method: "frappe.core.doctype.user.user.test_password_strength",
			args: {
				new_password: value || "",
			},
			callback: function (r) {
				if (r.message) {
					let score = r.message.score;
<<<<<<< HEAD
					var indicators = ["red", "red", "orange", "yellow", "green"];
=======
					var indicators = ["red", "red", "orange", "blue", "green"];
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
					me.set_strength_indicator(indicators[score]);
				}
			},
		});
	}
	set_strength_indicator(color) {
<<<<<<< HEAD
		var message = __("Include symbols, numbers and capital letters in the password");
		this.indicator.removeClass().addClass("password-strength-indicator indicator " + color);
=======
		let strength = {
			red: [__("Weak"), "danger", 25],
			orange: [__("Average"), "warning", 50],
			blue: [__("Strong"), "info", 75],
			green: [__("Excellent"), "success", 100],
		};
		let progress_text = strength[color][0];
		let progress_color = strength[color][1];
		let progress_percent = strength[color][2];

		this.indicator.removeClass("hidden");

		this.progress_text.html(progress_text).css("color", `var(--${color}-500)`);

		this.progress_bar
			.css("width", progress_percent + "%")
			.attr("aria-valuenow", progress_percent)
			.removeClass()
			.addClass("progress-bar progress-bar-" + progress_color);

		let message = __("Include symbols, numbers and capital letters in the password");
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
		this.message.html(message).toggleClass("hidden", color == "green");
	}
};
