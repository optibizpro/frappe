# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
import frappe.cache_manager
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestMilestoneTracker(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestMilestoneTracker(UnitTestCase):
	"""
	Unit tests for MilestoneTracker.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestMilestoneTracker(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def test_milestone(self):
		frappe.db.delete("Milestone Tracker")

		frappe.cache.delete_key("milestone_tracker_map")

		milestone_tracker = frappe.get_doc(
			doctype="Milestone Tracker", document_type="ToDo", track_field="status"
		).insert()

		todo = frappe.get_doc(doctype="ToDo", description="test milestone", status="Open").insert()

		milestones = frappe.get_all(
			"Milestone",
			fields=["track_field", "value", "milestone_tracker"],
			filters=dict(reference_type=todo.doctype, reference_name=todo.name),
		)

		self.assertEqual(len(milestones), 1)
		self.assertEqual(milestones[0].track_field, "status")
		self.assertEqual(milestones[0].value, "Open")

		todo.status = "Closed"
		todo.save()

		milestones = frappe.get_all(
			"Milestone",
			fields=["track_field", "value", "milestone_tracker"],
			filters=dict(reference_type=todo.doctype, reference_name=todo.name),
			order_by="creation desc",
		)

		self.assertEqual(len(milestones), 2)
		self.assertEqual(milestones[0].track_field, "status")
		self.assertEqual(milestones[0].value, "Closed")

		# cleanup
		frappe.db.delete("Milestone")
		milestone_tracker.delete()
