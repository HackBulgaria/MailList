class MailList():
    """docstring for MailList"""
    def __init__(self, list_id, name):
        self.__name = name
        self.__id = list_id
        self.subscribers = {}

    def add_subscriber(self, name, email):
        if email in self.subscribers:
            return False

        self.subscribers[email] = name
        return True

    def get_name(self):
        return self.__name

    def count(self):
        return len(self.subscribers)

    def get_subscriber_by_email(self, email):
        if email in self.subscribers:
            return (self.subscribers[email], email)

        return None

    def get_subscribers(self):
        result = []
        for email in self.subscribers:
            result.append((self.subscribers[email], email))
        return result

    def update_subscriber(self, email, update_hash):
        if "email" in update_hash:
            name = self.subscribers[email]
            self.subscribers[update_hash["email"]] = name
            del self.subscribers[email]
            email = update_hash["email"]

        if "name" in update_hash:
            self.subscribers[email] = update_hash["name"]

    def remove_subscriber(self, email):
        if email in self.subscribers:
            del self.subscribers[email]

        return None

    def get_id(self):
        return self.__id
