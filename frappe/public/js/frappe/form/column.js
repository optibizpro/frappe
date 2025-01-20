export default class Column {
	constructor(section, df) {
		if (!df) df = {};

		this.df = df;
		this.section = section;
		this.section.columns.push(this);
		this.make();
		this.resize_all_columns();
	}

	make() {
		this.wrapper = $(`
			<div class="form-column" data-fieldname="${this.df.fieldname}">
				<form>
				</form>
			</div>
		`).appendTo(this.section.body);

		this.form = this.wrapper.find("form").on("submit", () => false);

		if (this.df.description) {
			$(`
				<p class="col-sm-12 form-column-description">
					${__(this.df.description)}
				</p>
			`).prependTo(this.wrapper);
		}

		if (this.df.label) {
			$(`
				<label class="column-label">
					${__(this.df.label, null, this.df.parent)}
				</label>
<<<<<<< HEAD
			`).appendTo(this.wrapper);
=======
			`).prependTo(this.wrapper);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
		}
	}

	resize_all_columns() {
		// distribute all columns equally
		let columns = this.section.wrapper.find(".form-column").length;
		let colspan = cint(12 / columns);

		if (columns == 5) {
			colspan = 20;
		}

		this.section.wrapper
			.find(".form-column")
			.removeClass()
			.addClass("form-column")
			.addClass("col-sm-" + colspan);
	}

	add_field() {}

	refresh() {
		this.section.refresh();
	}
}
