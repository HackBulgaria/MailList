import unittest
from maillist import MailList


class MailListTest(unittest.TestCase):
    """docstring for MailListTest"""

    def setUp(self):
        # fuck static
        self.m = MailList(1, "Hack Bulgaria")

    def test_create_mail_list_get_name(self):
        self.assertEqual("Hack Bulgaria", self.m.get_name())

    def test_add_subscriber(self):
        self.m.add_subscriber("Rado", "radorado@hackbulgaria.com")

        self.assertEqual(1, self.m.count())

    def test_get_subscribers(self):
        self.m.add_subscriber("Rado", "radorado@hackbulgaria.com")

        expected = [("Rado", "radorado@hackbulgaria.com")]
        self.assertEqual(expected, self.m.get_subscribers())

    def test_get_id(self):
        self.assertEqual(1, self.m.get_id())

    def test_get_id_after_three_instances(self):
        m1 = MailList(1, "Hack")
        m2 = MailList(2, "Hack")
        m3 = MailList(3, "Hack")

        self.assertEqual(1, m1.get_id())
        self.assertEqual(2, m2.get_id())
        self.assertEqual(3, m3.get_id())
