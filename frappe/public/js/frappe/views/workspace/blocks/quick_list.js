import Block from "./block.js";
export default class QuickList extends Block {
	static get toolbox() {
		return {
			title: "Quick List",
			icon: frappe.utils.icon("list", "sm"),
		};
	}

	static get isReadOnlySupported() {
		return true;
	}

	constructor({ data, api, config, readOnly, block }) {
		super({ data, api, config, readOnly, block });
		this.col = this.data.col ? this.data.col : "4";
		this.allow_customization = !this.readOnly;
		this.options = {
			allow_sorting: this.allow_customization,
			allow_create: this.allow_customization,
			allow_delete: this.allow_customization,
			allow_hiding: false,
			allow_edit: true,
			allow_resize: true,
			min_width: 4,
			max_widget_count: 2,
		};
	}

	render() {
		this.wrapper = document.createElement("div");
		this.new("quick_list");

		if (this.data && this.data.quick_list_name) {
			let has_data = this.make("quick_list", this.data.quick_list_name);
<<<<<<< HEAD
			if (!has_data) return;
=======
			if (!has_data) return this.wrapper;
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		}

		if (!this.readOnly) {
			$(this.wrapper).find(".widget").addClass("quick_list edit-mode");
			this.add_settings_button();
			this.add_new_block_button();
		}

		return this.wrapper;
	}

	validate(savedData) {
		if (!savedData.quick_list_name) {
			return false;
		}

		return true;
	}

	save() {
		return {
			quick_list_name: this.wrapper.getAttribute("quick_list_name"),
			col: this.get_col(),
			new: this.new_block_widget,
		};
	}
}
