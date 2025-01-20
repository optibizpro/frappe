// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.ui.Tags = class {
	constructor({ parent, placeholder, tagsList, onTagAdd, onTagRemove, onTagClick, onChange }) {
		this.tagsList = tagsList || [];
		this.onTagAdd = onTagAdd;
		this.onTagRemove = onTagRemove;
		this.onTagClick = onTagClick;
		this.onChange = onChange;

		this.setup(parent, placeholder);
	}

	setup(parent, placeholder) {
		this.$ul = parent;
		this.$input = $(`<input class="tags-input form-control mt-2"></input>`);

		this.$inputWrapper = this.get_list_element(this.$input);
<<<<<<< HEAD
		this.$placeholder = this.get_list_element(
			$(`<span class="tags-placeholder text-muted">${placeholder}</span>`)
		);
=======
		this.$placeholder =
			$(`<button class="add-tags-btn text-muted btn btn-link icon-btn" id="add_tags">
				${__(placeholder)}
			</button>`);
		this.$placeholder.appendTo(this.$ul.find(".form-sidebar-items"));
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		this.$inputWrapper.appendTo(this.$ul);

		this.deactivate();
		this.bind();
		this.boot();
	}

	bind() {
		const me = this;
		const select_tag = function () {
			const tagValue = frappe.utils.xss_sanitise(me.$input.val());
			me.addTag(tagValue);
			me.$input.val("");
		};

		this.$input.keypress((e) => {
			if (e.which == 13 || e.keyCode == 13) select_tag();
		});
		this.$input.focusout(select_tag);

		this.$input.on("blur", () => {
			this.deactivate();
		});

		this.$placeholder.on("click", () => {
			this.activate();
			this.$input.focus(); // focus only when clicked
		});
	}

	boot() {
		this.addTags(this.tagsList);
	}

	activate() {
		this.$placeholder.hide();
		this.$inputWrapper.show();
	}

	deactivate() {
		this.$inputWrapper.hide();
		this.$placeholder.show();
	}

	addTag(label) {
		if (label && label !== "" && !this.tagsList.includes(label)) {
			let $tag = this.get_tag(label);
			let row = this.get_list_element($tag, "form-tag-row");
<<<<<<< HEAD
			row.insertBefore(this.$inputWrapper);
=======
			row.insertAfter(this.$inputWrapper);
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
			this.tagsList.push(label);
			this.onTagAdd && this.onTagAdd(label);
		}
	}

	removeTag(label) {
		label = frappe.utils.xss_sanitise(label);
		if (this.tagsList.includes(label)) {
			this.tagsList.splice(this.tagsList.indexOf(label), 1);
			this.onTagRemove && this.onTagRemove(label);
		}
	}

	addTags(labels) {
		labels.map(this.addTag.bind(this));
	}

	clearTags() {
		this.$ul.find(".form-tag-row").remove();
		this.tagsList = [];
	}

	get_list_element($element, class_name = "") {
<<<<<<< HEAD
		let $li = $(`<li class="${class_name}"></li>`);
=======
		let $li = $(`<div class="${class_name}"></div>`);
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		$element.appendTo($li);
		return $li;
	}

	get_tag(label) {
<<<<<<< HEAD
		let $tag = frappe.get_data_pill(label, label, (target, pill_wrapper) => {
			this.removeTag(target);
			pill_wrapper.closest(".form-tag-row").remove();
		});

=======
		let colored = true;
		let $tag = frappe.get_data_pill(
			label,
			label,
			(target, pill_wrapper) => {
				this.removeTag(target);
				pill_wrapper.closest(".form-tag-row").remove();
			},
			null,
			colored
		);
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
		if (this.onTagClick) {
			$tag.on("click", ".pill-label", () => {
				this.onTagClick(label);
			});
		}
		return $tag;
	}
};
