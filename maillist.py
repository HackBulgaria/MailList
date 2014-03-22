class MailList():
    """docstring for MailList"""
    def __init__(self, list_id, name):
        self.__name = name
        self.__id = list_id
        self.subscribers = {}

    def add_subscriber(self, name, email):
        self.subscribers[name] = email

    def get_name(self):
        return self.__name

    def count(self):
        return len(self.subscribers)

    def get_subscribers(self):
        result = []
        for name in self.subscribers:
            result.append((name, self.subscribers[name]))
        return result

    def get_id(self):
        return self.__id
