import unittest
from maillist import MailList


class MailListTest(unittest.TestCase):
    """docstring for MailListTest"""

    def test_create_mail_list_get_name(self):
        m = MailList("Hack Bulgaria")

        self.assertEqual("Hack Bulgaria", m.get_name())

if __name__ == '__main__':
    unittest.main()
