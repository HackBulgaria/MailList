import unittest
from commandparser import CommandParser


class CommandParserTest(unittest.TestCase):
    """docstring for CommandParserTest"""

    def setUp(self):
        self.cp = CommandParser()
        self.called = False

    def test_on_with_single_command(self):
        def callback(arguments):
            self.called = True
            self.assertEqual(0, len(arguments))

        self.cp.on("command", callback)
        self.cp.take_command("command")

        self.assertTrue(self.called)

    def test_on_with_full_command(self):
        def callback(arguments):
            self.called = True

            self.assertEqual(["1", "2"], arguments)

        self.cp.on("delete_subscriber", callback)
        self.cp.take_command("delete_subscriber 1 2")

        self.assertTrue(self.called)

    def test_on_with_command_not_found(self):
        def callback(arguments):
            self.called = True

        self.cp.on("something", callback)
        result = self.cp.take_command("something_else")

        self.assertFalse(self.called)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
