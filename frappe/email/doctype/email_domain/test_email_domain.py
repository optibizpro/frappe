# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.test_runner import make_test_objects
from frappe.tests.utils import FrappeTestCase

test_records = frappe.get_test_records("Email Domain")


class TestDomain(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase
from frappe.tests.utils import make_test_objects


class UnitTestEmailDomain(UnitTestCase):
	"""
	Unit tests for EmailDomain.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDomain(IntegrationTestCase):
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> fc1c3f895a2bbd99dd7a0574de180a4095b6e41b
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> e4a2b8db38691ac78018fd51fe0e037afbd14d87
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
	def setUp(self):
		make_test_objects("Email Domain", reset=True)

	def tearDown(self):
		frappe.delete_doc("Email Account", "Test")
		frappe.delete_doc("Email Domain", "test.com")

	def test_on_update(self):
		mail_domain = frappe.get_doc("Email Domain", "test.com")
		mail_account = frappe.get_doc("Email Account", "Test")

		# Ensure a different port
		mail_account.incoming_port = int(mail_domain.incoming_port) + 5
		mail_account.save()
		# Trigger update of accounts using this domain
		mail_domain.on_update()

		mail_account.reload()
		# After update, incoming_port in account should match the domain
		self.assertEqual(mail_account.incoming_port, mail_domain.incoming_port)

		# Also make sure that the other attributes match
		self.assertEqual(mail_account.use_imap, mail_domain.use_imap)
		self.assertEqual(mail_account.use_ssl, mail_domain.use_ssl)
		self.assertEqual(mail_account.use_starttls, mail_domain.use_starttls)
		self.assertEqual(mail_account.use_tls, mail_domain.use_tls)
		self.assertEqual(mail_account.attachment_limit, mail_domain.attachment_limit)
		self.assertEqual(mail_account.smtp_server, mail_domain.smtp_server)
		self.assertEqual(mail_account.smtp_port, mail_domain.smtp_port)
