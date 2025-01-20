frappe.provide("frappe.ui.misc");
frappe.ui.misc.about = function () {
	if (!frappe.ui.misc.about_dialog) {
<<<<<<< HEAD
		var d = new frappe.ui.Dialog({ title: __("Frappe Framework") });

		$(d.body).html(
			repl(
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
>>>>>>> obp-version-14
				"<div>\
		<p>" +
					__("Open Source Applications for the Web") +
					"</p>  \
		<p><i class='fa fa-globe fa-fw'></i>\
			Website: <a href='https://optibizpro.com' target='_blank'>https://optibizpro.com</a></p>\
		<p><i class='fa fa-github fa-fw'></i>\
			Source: <a href='https://github.com/optibizpro' target='_blank'>https://github.com/optibizpro</a></p>\
		<p><i class='fa fa-linkedin fa-fw'></i>\
			Linkedin: <a href='https://linkedin.com/company/optibizpro' target='_blank'>https://linkedin.com/company/optibizpro</a></p>\
		<p><i class='fa fa-facebook fa-fw'></i>\
			Facebook: <a href='https://facebook.com/optibizpro' target='_blank'>https://facebook.com/optibizpro</a></p>\
		<p><i class='fa fa-twitter fa-fw'></i>\
			Twitter: <a href='https://twitter.com/optibizpro' target='_blank'>https://twitter.com/optibizpro</a></p>\
		<hr>\
		<h4>Installed Apps</h4>\
		<div id='about-app-versions'>Loading versions...</div>\
		<hr>\
		<p class='text-muted'>&copy; Frappe Technologies Pvt. Ltd. and contributors </p> \
		</div>",
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
		var d = new frappe.ui.Dialog({ title: __("OptiBizPro") });

		$(d.body).html(
			repl(
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
				`<div>
					<p>${__("PT. OPTIMIZED BUSINESS PROCESS (OptiBizPro)")}</p>
					<p><i class='fa fa-globe fa-fw'></i>
						${__("Website")}:
						<a href='https://optibizpro.com' target='_blank'>https://optibizpro.com</a></p>
					<p><i class='fa fa-github fa-fw'></i>
						${__("Source")}:
						<a href='https://github.com/optibizpro' target='_blank'>https://github.com/optibizpro</a></p>
					<p><i class='fa fa-graduation-cap fa-fw'></i>
						Frappe School: <a href='https://optibizpro.school' target='_blank'>https://optibizpro.school</a></p>
					<p><i class='fa fa-linkedin fa-fw'></i>
						Linkedin: <a href='https://linkedin.com/company/optibizpro' target='_blank'>https://linkedin.com/company/optibizpro</a></p>
					<p><i class='fa fa-twitter fa-fw'></i>
						Twitter: <a href='https://twitter.com/optibizpro' target='_blank'>https://twitter.com/optibizpro</a></p>
					<p><i class='fa fa-youtube fa-fw'></i>
						YouTube: <a href='https://www.youtube.com/@optibizpro' target='_blank'>https://www.youtube.com/@optibizpro</a></p>
						<p><i class="fa-brands fa-tiktok"></i>
						TikTok: <a href='https://www.tiktok.com/@optibizpro' target='_blank'>https://www.tiktok.com/@optibizpro</a></p>
					<hr>
					<h4>${__("Installed Apps")}</h4>
					<div id='about-app-versions'>${__("Loading versions...")}</div>
					<p>
						<b>
							<a href="/attribution" target="_blank" class="text-muted">
								${__("Dependencies & Licenses")}
							</a>
						</b>
					</p>
					<hr>
					<p class='text-muted'>${__("&copy; Frappe Technologies Pvt. Ltd. and contributors")} </p>
					</div>`,
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
>>>>>>> obp-version-14
				frappe.app
			)
		);

		frappe.ui.misc.about_dialog = d;

		frappe.ui.misc.about_dialog.on_page_show = function () {
			if (!frappe.versions) {
				frappe.call({
					method: "frappe.utils.change_log.get_versions",
					callback: function (r) {
						show_versions(r.message);
					},
				});
			} else {
				show_versions(frappe.versions);
			}
		};

		var show_versions = function (versions) {
			var $wrap = $("#about-app-versions").empty();
			$.each(Object.keys(versions).sort(), function (i, key) {
				var v = versions[key];
				if (v.branch) {
					var text = $.format("<p><b>{0}:</b> v{1} ({2})<br></p>", [
<<<<<<< HEAD
=======
=======
				let text;
				if (v.branch) {
					text = $.format("<p><b>{0}:</b> v{1} ({2})<br></p>", [
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
>>>>>>> obp-version-14
						v.title,
						v.branch_version || v.version,
						v.branch,
					]);
				} else {
					var text = $.format("<p><b>{0}:</b> v{1}<br></p>", [v.title, v.version]);
<<<<<<< HEAD
=======
=======
					text = $.format("<p><b>{0}:</b> v{1}<br></p>", [v.title, v.version]);
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
>>>>>>> obp-version-14
				}
				$(text).appendTo($wrap);
			});

			frappe.versions = versions;
		};
	}

	frappe.ui.misc.about_dialog.show();
};
