import { create_default_layout, pluck } from "./utils";
import { watch, ref, inject, computed, nextTick } from "vue";

export function getStore(print_format_name) {
	// variables
	let letterhead_name = ref(null);
	let print_format = ref(null);
	let letterhead = ref(null);
	let doctype = ref(null);
	let meta = ref(null);
	let layout = ref(null);
	let dirty = ref(false);
	let edit_letterhead = ref(false);

<<<<<<< HEAD
	let options = {
		data() {
			return {
				print_format_name,
				letterhead_name: null,
				print_format: null,
				letterhead: null,
				doctype: null,
				meta: null,
				layout: null,
				dirty: false,
				edit_letterhead: false,
			};
		},
		watch: {
			layout: {
				deep: true,
				handler() {
					this.dirty = true;
				},
			},
			print_format: {
				deep: true,
				handler() {
					this.dirty = true;
				},
			},
		},
		methods: {
			fetch() {
				return new Promise((resolve) => {
					frappe.model.clear_doc("Print Format", this.print_format_name);
					frappe.model.with_doc("Print Format", this.print_format_name, () => {
						let print_format = frappe.get_doc("Print Format", this.print_format_name);
						frappe.model.with_doctype(print_format.doc_type, () => {
							this.meta = frappe.get_meta(print_format.doc_type);
							this.print_format = print_format;
							this.layout = this.get_layout();
							this.$nextTick(() => (this.dirty = false));
							this.edit_letterhead = false;
							resolve();
						});
					});
=======
	// methods
	function fetch() {
		return new Promise((resolve) => {
			frappe.model.clear_doc("Print Format", print_format_name);
			frappe.model.with_doc("Print Format", print_format_name, () => {
				let _print_format = frappe.get_doc("Print Format", print_format_name);
				frappe.model.with_doctype(_print_format.doc_type, () => {
					meta.value = frappe.get_meta(_print_format.doc_type);
					print_format.value = _print_format;
					layout.value = get_layout();
					nextTick(() => (dirty.value = false));
					edit_letterhead.value = false;
					resolve();
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
				});
			});
		});
	}
	function update({ fieldname, value }) {
		print_format.value[fieldname] = value;
	}
	function save_changes() {
		frappe.dom.freeze(__("Saving..."));

<<<<<<< HEAD
				this.layout.sections = this.layout.sections
					.filter((section) => !section.remove)
					.map((section) => {
						section.columns = section.columns.map((column) => {
							column.fields = column.fields
								.filter((df) => !df.remove)
								.map((df) => {
									if (df.table_columns) {
										df.table_columns = df.table_columns.map((tf) => {
											return pluck(tf, [
												"label",
												"fieldname",
												"fieldtype",
												"options",
												"width",
												"field_template",
											]);
										});
									}
									return pluck(df, [
=======
		layout.value.sections = layout.value.sections
			.filter((section) => !section.remove)
			.map((section) => {
				section.columns = section.columns.map((column) => {
					column.fields = column.fields
						.filter((df) => !df.remove)
						.map((df) => {
							if (df.table_columns) {
								df.table_columns = df.table_columns.map((tf) => {
									return pluck(tf, [
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
										"label",
										"fieldname",
										"fieldtype",
										"options",
<<<<<<< HEAD
										"table_columns",
										"html",
=======
										"width",
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
										"field_template",
									]);
								});
							}
							return pluck(df, [
								"label",
								"fieldname",
								"fieldtype",
								"options",
								"table_columns",
								"html",
								"field_template",
							]);
						});
					return column;
				});
				return section;
			});

		print_format.value.format_data = JSON.stringify(layout.value);

<<<<<<< HEAD
				frappe
					.call("frappe.client.save", {
						doc: this.print_format,
					})
					.then(() => {
						if (this.letterhead && this.letterhead._dirty) {
							return frappe
								.call("frappe.client.save", {
									doc: this.letterhead,
								})
								.then((r) => (this.letterhead = r.message));
						}
					})
					.then(() => this.fetch())
					.always(() => {
						frappe.dom.unfreeze();
						this.$emit("after_save");
					});
			},
			reset_changes() {
				this.fetch();
			},
			get_layout() {
				if (this.print_format) {
					if (typeof this.print_format.format_data == "string") {
						return JSON.parse(this.print_format.format_data);
					}
					return this.print_format.format_data;
				}
				return null;
			},
			get_default_layout() {
				return create_default_layout(this.meta, this.print_format);
			},
			change_letterhead(letterhead) {
				return frappe.db.get_doc("Letter Head", letterhead).then((doc) => {
					this.letterhead = doc;
				});
			},
		},
=======
		frappe
			.call("frappe.client.save", {
				doc: print_format.value,
			})
			.then(() => {
				if (letterhead.value && letterhead.value._dirty) {
					return frappe
						.call("frappe.client.save", {
							doc: letterhead.value,
						})
						.then((r) => (letterhead.value = r.message));
				}
			})
			.then(() => fetch())
			.always(() => {
				frappe.dom.unfreeze();
			});
	}
	function reset_changes() {
		fetch();
	}
	function get_layout() {
		if (print_format.value) {
			if (typeof print_format.value.format_data == "string") {
				return JSON.parse(print_format.value.format_data);
			}
			return print_format.value.format_data;
		}
		return null;
	}
	function get_default_layout() {
		return create_default_layout(meta.value, print_format.value);
	}
	function change_letterhead(_letterhead) {
		return frappe.db.get_doc("Letter Head", _letterhead).then((doc) => {
			letterhead.value = doc;
		});
	}

	// watch
	watch(layout, () => {
		dirty.value = true;
	});
	watch(print_format, () => {
		dirty.value = true;
	});

	return {
		letterhead_name,
		print_format,
		letterhead,
		doctype,
		meta,
		layout,
		dirty,
		edit_letterhead,
		fetch,
		update,
		save_changes,
		reset_changes,
		get_layout,
		get_default_layout,
		change_letterhead,
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
	};
}

<<<<<<< HEAD
export let storeMixin = {
	inject: ["$store"],
	computed: {
		print_format() {
			return this.$store.print_format;
		},
		layout() {
			return this.$store.layout;
		},
		letterhead() {
			return this.$store.letterhead;
		},
		meta() {
			return this.$store.meta;
		},
	},
};
=======
export function useStore() {
	// inject store
	let store = ref(inject("$store"));

	// computed
	let print_format = computed(() => {
		return store.value.print_format;
	});
	let layout = computed(() => {
		return store.value.layout;
	});
	let letterhead = computed(() => {
		return store.value.letterhead;
	});
	let meta = computed(() => {
		return store.value.meta;
	});

	return { print_format, layout, letterhead, meta, store };
}
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
