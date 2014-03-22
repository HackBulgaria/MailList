from maillist_factory import MailListFactory
from maillist_file_adapter import MailListFileAdapter
import unittest
import os


class MailListFileAdapterTest(unittest.TestCase):
    """docstring for MailListFileAdapterTest"""
    def setUp(self):
        self.factory = MailListFactory()
        self.m = self.factory.create("Hack Bulgaria")
        self.m.add_subscriber("Rado", "rado@rado")
        self.m.add_subscriber("Ivan", "ivan@ivan")

        self.maillist_adapter = MailListFileAdapter(self.m)

    def test_get_file_name(self):
        self.assertEqual("Hack_Bulgaria",
                         self.maillist_adapter.get_file_name())

    def test_prepare_for_save(self):
        expected = sorted(["Rado - rado@rado", "Ivan - ivan@ivan"])
        self.assertEqual(expected, self.maillist_adapter.prepare_for_save())

    def test_save_id_on_first_line(self):
        file_name = self.maillist_adapter.get_file_name()
        self.maillist_adapter.save()

        file = open(file_name, "r")
        contents = file.read()
        file.close()

        lines = contents.split("\n")
        self.assertEqual("1", lines[0])

    def test_save_contents_format(self):
        file_name = self.maillist_adapter.get_file_name()
        self.maillist_adapter.save()
        file = open(file_name, "r")
        contents = file.read()
        lines = contents.split("\n")
        file.close()

        expected = sorted(["Rado - rado@rado", "Ivan - ivan@ivan"])
        expected = "\n".join(expected)
        lines.pop(0)  # remove the id

        self.assertEqual(expected, "\n".join(lines))

    def test_load_from_file(self):
        m = self.factory.create("Hack Bulgaria")
        m.add_subscriber("Ivo", "ivo@ivo.com")
        m.add_subscriber("Maria", "maria@maria.com")
        file_adapter = MailListFileAdapter(m)
        file_name = file_adapter.get_file_name()

        file_adapter.save()

        loaded_mail_list = file_adapter.load(file_name)

        self.assertEqual(m.get_id(), loaded_mail_list.get_id())
        self.assertEqual(m.get_name(), loaded_mail_list.get_name())
        self.assertEqual(m.get_subscribers(),
                         loaded_mail_list.get_subscribers())

        os.remove(file_name)

    def tearDown(self):
        try:
            os.remove(self.maillist_adapter.get_file_name())
        except Exception:
            pass
