from commandparser import CommandParser
from maillist_factory import MailListFactory
from maillist_file_adapter import MailListFileAdapter
from glob import glob
from os.path import basename
import sys


class MailListProgram():
    """docstring for MailListProgram"""
    def __init__(self):
        self.factory = MailListFactory()
        self.cp = CommandParser()
        self.lists = {}
        self.db_path = "lists/"

        self._load_initial_state()
        self._init_callbacks()
        self._loop()

    def create_list_callback(self, arguments):
        name = " ".join(arguments)

        maillist = self.factory.create(name)
        maillist_adapter = MailListFileAdapter(self.db_path, maillist)
        maillist_adapter.save()

        self.lists[maillist.get_id()] = (maillist, maillist_adapter)

    def add_subscriber_callback(self, arguments):
        list_id = int("".join(arguments))
        name = input("name>")
        email = input("email>")

        self.lists[list_id][0].add_subscriber(name, email)
        self._notify_save(list_id)

    def show_lists_callback(self, arguments):
        for list_id in self.lists:
            current_list = self.lists[list_id][0]
            print("[{}] {}".format(list_id,
                                   current_list.get_name()))

    def show_list_callback(self, arguments):
        list_id = int("".join(arguments))

        if list_id in self.lists:
            subscribers = self.lists[list_id][0].get_subscribers()
            for s in subscribers:
                print("{} - {}".format(s[0], s[1]))
        else:
            print("List with id <{}> was not found".format(list_id))

    def exit_callback(self, arguments):
        sys.exit(0)

    def _load_initial_state(self):
        dir_lists = map(basename, glob(self.db_path + "*"))

        for list_file in dir_lists:
            adapter = MailListFileAdapter(self.db_path)
            parsed_list = adapter.load(list_file)

            maillist_adapter = MailListFileAdapter(self.db_path, parsed_list)

            self.lists[parsed_list.get_id()] = (parsed_list, maillist_adapter)

    def _init_callbacks(self):
        self.cp.on("create", self.create_list_callback)
        self.cp.on("add", self.add_subscriber_callback)
        self.cp.on("show_lists", self.show_lists_callback)
        self.cp.on("show_list", self.show_list_callback)
        self.cp.on("exit", self.exit_callback)
        # TODO - implement the rest of the callbacks

    def _notify_save(self, list_id):
        self.lists[list_id][1].save()

    def _loop(self):
        while True:
            command = input(">")
            self.cp.take_command(command)


if __name__ == '__main__':
    MailListProgram()
