import unittest
from maillist_factory import MailListFactory


class MailListFactoryTest(unittest.TestCase):
    """docstring for MailListFactoryTest"""

    def setUp(self):
        self.factory = MailListFactory()

    def test_get_next_id(self):
        self.assertEqual(1, self.factory.next_id())

    def test_create_new_mail_list(self):
        m = self.factory.create("Hack Bulgaria")

        self.assertEqual("Hack Bulgaria", m.get_name())
        self.assertEqual(1, m.get_id())
