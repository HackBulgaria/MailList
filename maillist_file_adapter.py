from maillist import MailList


class MailListFileAdapter():
    """docstring for MailListFileAdapter"""
    def __init__(self, mail_list):
        self.mail_list = mail_list

    def get_file_name(self):
        return self.mail_list.get_name().replace(" ", "_")

    # (name, email) -> "<name> - <email>"
    def prepare_for_save(self):
        subscribers = self.mail_list.get_subscribers()
        subscribers = map(lambda t: "{} - {}".format(t[0], t[1]), subscribers)

        return sorted(subscribers)

    def save(self):
        file_to_save = open(self.get_file_name(), "w")
        contents = "{}\n".format(self.mail_list.get_id())
        contents += "\n".join(self.prepare_for_save())

        file_to_save.write(contents)
        file_to_save.close()

    def load(self, file_name):
        file = open(file_name, "r")
        contents = file.read()
        file.close()

        lines = contents.split("\n")

        maillist_name = file_name.replace("_", " ")
        maillist_id = int(lines[0])
        lines.pop(0)

        ## should be
        ## MailListFactory.create_with_id(.. ..)
        result = MailList(maillist_id, maillist_name)

        for unparsed_subscriber in lines:
            subscriber = unparsed_subscriber.split(" - ")
            result.add_subscriber(subscriber[0], subscriber[1])

        return result
