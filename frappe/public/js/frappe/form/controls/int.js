frappe.ui.form.ControlInt = class ControlInt extends frappe.ui.form.ControlData {
	static trigger_change_on_input_event = false;
<<<<<<< HEAD
=======
	static input_mode = "numeric";
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	make() {
		super.make();
	}
	make_input() {
<<<<<<< HEAD
		var me = this;
		super.make_input();
		this.$input
			// .addClass("text-right")
			.on("focus", function () {
				setTimeout(function () {
					if (!document.activeElement) return;
					document.activeElement.value = me.validate(document.activeElement.value);
					document.activeElement.select();
				}, 100);
				return false;
			});
=======
		super.make_input();
		this.$input.on("focus", () => {
			document.activeElement?.select?.();
			return false;
		});
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	}
	validate(value) {
		return this.parse(value);
	}
	eval_expression(value) {
		if (typeof value === "string") {
<<<<<<< HEAD
			if (value.match(/^[0-9+\-/* ]+$/)) {
=======
			const parsed_components = value.match(/[^\d.,]+|[\d.,]+/g);
			var parsed_value = value;
			if (parsed_components !== null) {
				parsed_value = parsed_components
					.map((v) => {
						return isNaN(parseFloat(v)) ? v : flt(v);
					})
					.join("");
			}
			if (parsed_value.match(/^[0-9+\-/*.() ]+$/)) {
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
				// If it is a string containing operators
				try {
					return eval(parsed_value);
				} catch (e) {
					// bad expression
					return value;
				}
			}
		}
		return value;
	}
	parse(value) {
		return cint(this.eval_expression(value), null);
	}
};

frappe.ui.form.ControlLongInt = frappe.ui.form.ControlInt;
