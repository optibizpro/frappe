// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

frappe.provide("frappe.views.calendar");
frappe.provide("frappe.views.calendars");

frappe.views.CalendarView = class CalendarView extends frappe.views.ListView {
	static load_last_view() {
		const route = frappe.get_route();
		if (route.length === 3) {
			const doctype = route[1];
			const user_settings = frappe.get_user_settings(doctype)["Calendar"] || {};
			route.push(user_settings.last_calendar || "default");
			frappe.route_flags.replace_route = true;
			frappe.set_route(route);
			return true;
		} else {
			return false;
		}
	}

	toggle_result_area() {}

	get view_name() {
		return "Calendar";
	}

	setup_defaults() {
		return super.setup_defaults().then(() => {
			this.page_title = __("{0} Calendar", [this.page_title]);
<<<<<<< HEAD
			this.calendar_settings = frappe.views.calendar[this.doctype] || {};
=======
			this.calendar_settings = frappe.views.Calendar[this.doctype] || {};
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			this.calendar_name = frappe.get_route()[3];
		});
	}

	setup_page() {
		this.hide_page_form = true;
		super.setup_page();
	}

	setup_view() {}

	before_render() {
		super.before_render();
		this.save_view_user_settings({
			last_calendar: this.calendar_name,
		});
	}

	render() {
		if (this.calendar) {
			this.calendar.refresh();
			return;
		}

		this.load_lib
			.then(() => this.get_calendar_preferences())
			.then((options) => {
				this.calendar = new frappe.views.Calendar(options);
			});
	}

	get_calendar_preferences() {
		const options = {
			doctype: this.doctype,
			parent: this.$result,
			page: this.page,
			list_view: this,
		};
		const calendar_name = this.calendar_name;

		return new Promise((resolve) => {
			if (calendar_name === "default") {
				Object.assign(options, frappe.views.calendar[this.doctype]);
				resolve(options);
			} else {
				frappe.model.with_doc("Calendar View", calendar_name, () => {
					const doc = frappe.get_doc("Calendar View", calendar_name);
					if (!doc) {
						frappe.show_alert(
							__("{0} is not a valid Calendar. Redirecting to default Calendar.", [
								calendar_name.bold(),
							])
						);
						frappe.set_route("List", this.doctype, "Calendar", "default");
						return;
					}
					Object.assign(options, {
						field_map: {
							id: "name",
							start: doc.start_date_field,
							end: doc.end_date_field,
							title: doc.subject_field,
							allDay: doc.all_day ? 1 : 0,
						},
					});
					resolve(options);
				});
			}
		});
	}

	get required_libs() {
<<<<<<< HEAD
		let assets = [
			"assets/frappe/js/lib/fullcalendar/fullcalendar.min.css",
			"assets/frappe/js/lib/fullcalendar/fullcalendar.min.js",
		];
		let user_language = frappe.boot.user.language;
		if (user_language && user_language !== "en") {
			assets.push("assets/frappe/js/lib/fullcalendar/locale-all.js");
		}
		return assets;
=======
		return "calendar.bundle.js";
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	}
};

frappe.views.Calendar = class Calendar {
	constructor(options) {
		$.extend(this, options);
		this.field_map = this.field_map || {
			id: "name",
			start: "start",
			end: "end",
			allDay: "all_day",
			convertToUserTz: "convert_to_user_tz",
		};
		this.color_map = {
			danger: "red",
			success: "green",
			warning: "orange",
			default: "blue",
		};
		this.get_default_options();
	}
	get_default_options() {
		return new Promise((resolve) => {
<<<<<<< HEAD
			let defaultView = localStorage.getItem("cal_defaultView");
			let weekends = localStorage.getItem("cal_weekends");
			let defaults = {
				defaultView: defaultView ? defaultView : "month",
=======
			let initialView = localStorage.getItem("cal_initialView");
			let weekends = localStorage.getItem("cal_weekends");
			let defaults = {
				initialView: initialView ? initialView : "dayGridMonth",
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
				weekends: weekends ? weekends : true,
			};
			resolve(defaults);
		}).then((defaults) => {
			this.make_page();
			this.setup_options(defaults);
			this.make();
			this.setup_view_mode_button(defaults);
			this.bind();
		});
	}
	make_page() {
		var me = this;

		// add links to other calendars
		me.page.clear_user_actions();
		$.each(frappe.boot.calendars, function (i, doctype) {
			if (frappe.model.can_read(doctype)) {
				me.page.add_menu_item(__(doctype), function () {
					frappe.set_route("List", doctype, "Calendar");
				});
			}
		});

		$(this.parent).on("show", function () {
<<<<<<< HEAD
			me.$cal.fullCalendar("refetchEvents");
=======
			me.$cal.fullCalendar.refetchEvents();
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		});
	}

	make() {
		this.$wrapper = this.parent;
<<<<<<< HEAD
		this.$cal = $("<div>").appendTo(this.$wrapper);
=======
		this.$cal = $("<div id='fc-calendar-wrapper'>").appendTo(this.$wrapper);
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		this.footnote_area = frappe.utils.set_footnote(
			this.footnote_area,
			this.$wrapper,
			__("Select or drag across time slots to create a new event.")
		);
		this.footnote_area.css({ "border-top": "0px" });
<<<<<<< HEAD
=======

		this.fullCalendar = new frappe.FullCalendar(this.$cal[0], this.cal_options);
		this.fullCalendar.render();
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581

		this.set_css();
	}
	setup_view_mode_button(defaults) {
		var me = this;
		$(me.footnote_area).find(".btn-weekend").detach();
		let btnTitle = defaults.weekends ? __("Hide Weekends") : __("Show Weekends");
		const btn = `<button class="btn btn-default btn-xs btn-weekend">${btnTitle}</button>`;
		me.footnote_area.append(btn);
	}
	set_localStorage_option(option, value) {
		localStorage.removeItem(option);
		localStorage.setItem(option, value);
	}
	bind() {
		const me = this;
		let btn_group = me.$wrapper.find(".fc-button-group");
		btn_group.on("click", ".btn", function () {
<<<<<<< HEAD
			let value = $(this).hasClass("fc-agendaWeek-button")
				? "agendaWeek"
				: $(this).hasClass("fc-agendaDay-button")
				? "agendaDay"
				: "month";
			me.set_localStorage_option("cal_defaultView", value);
=======
			let value = $(this).hasClass("fc-dayGridWeek-button")
				? "dayGridWeek"
				: $(this).hasClass("fc-dayGridDay-button")
				? "dayGridDay"
				: "dayGridMonth";
			me.set_localStorage_option("cal_initialView", value);
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		});

		me.$wrapper.on("click", ".btn-weekend", function () {
			me.cal_options.weekends = !me.cal_options.weekends;
<<<<<<< HEAD
			me.$cal.fullCalendar("option", "weekends", me.cal_options.weekends);
=======
			me.fullCalendar.setOption("weekends", me.cal_options.weekends);
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			me.set_localStorage_option("cal_weekends", me.cal_options.weekends);
			me.set_css();
			me.setup_view_mode_button(me.cal_options);
		});
	}
	set_css() {
<<<<<<< HEAD
		// flatify buttons
		this.$wrapper
			.find("button.fc-state-default")
			.removeClass("fc-state-default")
=======
		const viewButtons =
			".fc-dayGridMonth-button, .fc-dayGridWeek-button, .fc-dayGridDay-button, .fc-today-button";
		const fcViewButtonClasses = "fc-button fc-button-primary fc-button-active";

		// remove fc-button styles
		this.$wrapper
			.find("button.fc-button")
			.removeClass(fcViewButtonClasses)
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			.addClass("btn btn-default");

		// group all view buttons
		this.$wrapper.find(viewButtons).wrapAll('<div class="btn-group" />');

		// add icons
		this.$wrapper
<<<<<<< HEAD
			.find(".fc-month-button, .fc-agendaWeek-button, .fc-agendaDay-button")
			.wrapAll('<div class="btn-group" />');

		this.$wrapper
			.find(".fc-prev-button span")
			.attr("class", "")
			.html(frappe.utils.icon("left"));
		this.$wrapper
			.find(".fc-next-button span")
			.attr("class", "")
			.html(frappe.utils.icon("right"));

		this.$wrapper.find(".fc-today-button").prepend(frappe.utils.icon("today"));

		this.$wrapper.find(".fc-day-number").wrap('<div class="fc-day"></div>');
=======
			.find(`.fc-prev-button span`)
			.attr("class", "")
			.html(frappe.utils.icon("left"));
		this.$wrapper
			.find(`.fc-next-button span`)
			.attr("class", "")
			.html(frappe.utils.icon("right"));
		if (this.$wrapper.find(".fc-today-button svg").length == 0)
			this.$wrapper.find(".fc-today-button").prepend(frappe.utils.icon("today"));
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581

		// v6.x of fc has weird behaviour which removes all the custom classes
		// on header buttons on click, event below re-adds all the classes
		var btn_group = this.$wrapper.find(".fc-button-group");
		btn_group.find(".fc-button-active").addClass("active");

		btn_group.find(".btn").on("click", function () {
			btn_group
				.find(viewButtons)
				.removeClass(`active ${fcViewButtonClasses}`)
				.addClass("btn btn-default");

<<<<<<< HEAD
		btn_group.find(".btn").on("click", function () {
			btn_group.find(".btn").removeClass("active");
=======
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			$(this).addClass("active");
		});
	}

	get_system_datetime(date) {
<<<<<<< HEAD
		date._offset = moment(date).tz(frappe.sys_defaults.time_zone)._offset;
		return frappe.datetime.convert_to_system_tz(moment(date).locale("en"));
=======
<<<<<<< HEAD
		date._offset = moment(date).tz(frappe.sys_defaults.time_zone)._offset;
		return frappe.datetime.convert_to_system_tz(moment(date).locale("en"));
=======
		return frappe.datetime.convert_to_system_tz(date, true);
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	}
	setup_options(defaults) {
		var me = this;
		defaults.meridiem = "false";
		this.cal_options = {
<<<<<<< HEAD
			locale: frappe.boot.user.language || "en",
			header: {
				left: "prev, title, next",
				right: "today, month, agendaWeek, agendaDay",
=======
			plugins: frappe.FullCalendar.Plugins,
			initialView: defaults.initialView || "dayGridMonth",
			locale: frappe.boot.lang,
			firstDay: 1,
			headerToolbar: {
				left: "prev,title,next",
				center: "",
				right: "today,dayGridMonth,dayGridWeek,dayGridDay",
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			},
			editable: true,
			droppable: true,
			selectable: true,
			selectMirror: true,
			forceEventDuration: true,
			displayEventTime: true,
			weekends: defaults.weekends,
			nowIndicator: true,
<<<<<<< HEAD
=======
			themeSystem: null,
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			buttonText: {
				today: __("Today"),
				month: __("Month"),
				week: __("Week"),
				day: __("Day"),
			},
<<<<<<< HEAD
			events: function (start, end, timezone, callback) {
				return frappe.call({
					method: me.get_events_method || "frappe.desk.calendar.get_events",
					type: "GET",
					args: me.get_args(start, end),
					callback: function (r) {
						var events = r.message || [];
						events = me.prepare_events(events);
						callback(events);
=======
			events: function (info, successCallback, failureCallback) {
				return frappe.call({
					method: me.get_events_method || "frappe.desk.calendar.get_events",
					type: "GET",
					args: me.get_args(info.start, info.end),
					callback: function (r) {
						var events = r.message || [];
						events = me.prepare_events(events);
						successCallback(events);
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
					},
				});
			},
			displayEventEnd: true,
<<<<<<< HEAD
			eventRender: function (event, element) {
				element.attr("title", event.tooltip);
			},
			eventClick: function (event) {
				// edit event description or delete
				var doctype = event.doctype || me.doctype;
				if (frappe.model.can_read(doctype)) {
					frappe.set_route("Form", doctype, event.name);
				}
			},
			eventDrop: function (event, delta, revertFunc) {
				me.update_event(event, revertFunc);
			},
			eventResize: function (event, delta, revertFunc) {
				me.update_event(event, revertFunc);
			},
			select: function (startDate, endDate, jsEvent, view) {
				if (view.name === "month" && endDate - startDate === 86400000) {
=======
			eventClick: function (info) {
				// edit event description or delete
				var doctype = info.doctype || me.doctype;
				if (frappe.model.can_read(doctype)) {
					frappe.set_route("Form", doctype, info.event.id);
				}
			},
			eventDrop: function (info) {
				me.update_event(info.event, info.revert);
			},
			eventResize: function (info) {
				me.update_event(info.event, info.revert);
			},
			select: function (info) {
				const seconds = info.end - info.start;
				const allDay = seconds === 86400000;

				if (info.view.type === "dayGridMonth" && allDay) {
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
					// detect single day click in month view
					return;
				}

				var event = frappe.model.get_new_doc(me.doctype);

				event[me.field_map.start] = me.get_system_datetime(info.start);
				if (me.field_map.end) event[me.field_map.end] = me.get_system_datetime(info.end);

<<<<<<< HEAD
				if (me.field_map.end) event[me.field_map.end] = me.get_system_datetime(endDate);

				if (me.field_map.allDay) {
					var all_day = startDate._ambigTime && endDate._ambigTime ? 1 : 0;

					event[me.field_map.allDay] = all_day;

					if (all_day)
						event[me.field_map.end] = me.get_system_datetime(
							moment(endDate).subtract(1, "s")
						);
=======
				if (seconds >= 86400000) {
					if (allDay) {
						// all-day click
						event[me.field_map.allDay] = 1;
					}
					// incase of all day or multiple day events -1 sec
					event[me.field_map.end] = me.get_system_datetime(info.end - 1);
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
				}
				frappe.set_route("Form", me.doctype, event.name);
			},
<<<<<<< HEAD
			dayClick: function (date, jsEvent, view) {
				if (view.name === "month") {
					const $date_cell = $("td[data-date=" + date.format("YYYY-MM-DD") + "]");

					if ($date_cell.hasClass("date-clicked")) {
						me.$cal.fullCalendar("changeView", "agendaDay");
						me.$cal.fullCalendar("gotoDate", date);
=======
			dateClick: function (info) {
				if (info.view.type === "dayGridMonth") {
					const $date_cell = $(
						"td[data-date=" + info.date.toISOString().slice(0, 10) + "]"
					);

					if ($date_cell.hasClass("date-clicked")) {
						me.fullCalendar.changeView("timeGridDay", info.date);
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
						me.$wrapper.find(".date-clicked").removeClass("date-clicked");

						// update "active view" btn
						me.$wrapper.find(".fc-month-button").removeClass("active");
						me.$wrapper.find(".fc-agendaDay-button").addClass("active");
					}

					me.$wrapper.find(".date-clicked").removeClass("date-clicked");
					$date_cell.addClass("date-clicked");
<<<<<<< HEAD
=======

					// explicitly remove the fc primary button styling that is append on view change
					// from month -> day
					$("#fc-calendar-wrapper")
						.find("button.fc-button")
						.removeClass("fc-button fc-button-primary fc-button-active")
						.addClass("btn btn-default");
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
				}
				return false;
			},
		};

		if (this.options) {
			$.extend(this.cal_options, this.options);
		}
	}
	get_args(start, end) {
		var args = {
			doctype: this.doctype,
			start: this.get_system_datetime(start),
			end: this.get_system_datetime(end),
			fields: this.fields,
			filters: this.list_view.filter_area.get(),
			field_map: this.field_map,
		};
		return args;
	}
	refresh() {
<<<<<<< HEAD
		this.$cal.fullCalendar("refetchEvents");
=======
		this.fullCalendar.refetchEvents();
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
	}
	prepare_events(events) {
		var me = this;

		return (events || []).map((d) => {
			d.id = d.name;
			d.editable = frappe.model.can_write(d.doctype || me.doctype);

			// do not allow submitted/cancelled events to be moved / extended
			if (d.docstatus && d.docstatus > 0) {
				d.editable = false;
			}

			$.each(me.field_map, function (target, source) {
				d[target] = d[source];
			});

			if (typeof d.allDay === "undefined") {
				d.allDay = me.field_map.allDay;
			}

			if (!me.field_map.convertToUserTz) d.convertToUserTz = 1;

			// convert to user tz
			if (d.convertToUserTz) {
				d.start = frappe.datetime.convert_to_user_tz(d.start);
				d.end = frappe.datetime.convert_to_user_tz(d.end);
			}

			// show event on single day if start or end date is invalid
			if (!frappe.datetime.validate(d.start) && d.end) {
				d.start = frappe.datetime.add_days(d.end, -1);
			}

			if (d.start && !frappe.datetime.validate(d.end)) {
				d.end = frappe.datetime.add_days(d.start, 1);
			}

			me.prepare_colors(d);

			d.title = frappe.utils.html2text(d.title);

			return d;
		});
	}
	prepare_colors(d) {
		let color, color_name;
		if (this.get_css_class) {
			color_name = this.color_map[this.get_css_class(d)] || "blue";

			if (color_name.startsWith("#")) {
				color_name = frappe.ui.color.validate_hex(color_name) ? color_name : "blue";
			}

			d.backgroundColor = frappe.ui.color.get(color_name, "extra-light");
			d.textColor = frappe.ui.color.get(color_name, "dark");
		} else {
			color = d.color;
			if (!frappe.ui.color.validate_hex(color) || !color) {
				color = frappe.ui.color.get("blue", "extra-light");
			}
			d.backgroundColor = color;
			d.textColor = frappe.ui.color.get_contrast_color(color);
		}
		return d;
	}
	update_event(event, revertFunc) {
		var me = this;
		frappe.model.remove_from_locals(me.doctype, event.id);
		return frappe.call({
			method: me.update_event_method || "frappe.desk.calendar.update_event",
			args: me.get_update_args(event),
			callback: function (r) {
				if (r.exc) {
					frappe.show_alert(__("Unable to update event"));
					revertFunc();
				}
			},
			error: function () {
				revertFunc();
			},
		});
	}
	get_update_args(event) {
		var me = this;
		var args = {
<<<<<<< HEAD
			name: event[this.field_map.id],
=======
			name: event.id,
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
		};

		args[this.field_map.start] = me.get_system_datetime(event.start);

<<<<<<< HEAD
		if (this.field_map.allDay)
			args[this.field_map.allDay] = event.start._ambigTime && event.end._ambigTime ? 1 : 0;
=======
		if (this.field_map.allDay) {
			args[this.field_map.allDay] = event.end - event.start === 86400000 ? 1 : 0;
		}
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581

		if (this.field_map.end) {
			if (!event.end) {
				event.end = event.start.add(1, "hour");
			}

			args[this.field_map.end] = me.get_system_datetime(event.end);
			if (args[this.field_map.allDay]) {
<<<<<<< HEAD
				args[this.field_map.end] = me.get_system_datetime(
					moment(event.end).subtract(1, "s")
				);
=======
				args[this.field_map.end] = me.get_system_datetime(new Date(event.end - 1000));
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
			}
		}

		args.doctype = event.doctype || this.doctype;

		return { args: args, field_map: this.field_map };
	}
<<<<<<< HEAD

	fix_end_date_for_event_render(event) {
		if (event.allDay) {
			// We use inclusive end dates. This workaround fixes the rendering of events
			event.start = event.start ? $.fullCalendar.moment(event.start).stripTime() : null;
			event.end = event.end
				? $.fullCalendar.moment(event.end).add(1, "day").stripTime()
				: null;
		}
	}
=======
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
};
