from maillist import MailList


class MailListFactory():
    """docstring for MailListFactory"""
    def __init__(self):
        self.__current_id = 1
        pass

    def next_id(self):
        result = self.__current_id
        self.__current_id += 1

        return result

    def create(self, list_name):
        m = MailList(self.next_id(), list_name)
        return m
