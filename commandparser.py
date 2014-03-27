class CommandParser(object):
    """docstring for CommandParser"""
    def __init__(self):
        self.callback_hash = {}

    def on(self, command, callback):
        self.callback_hash[command] = callback

    def take_command(self, unparsed_command):
        command_parts = unparsed_command.split(" ")
        arguments = command_parts[1:]

        if command_parts[0] in self.callback_hash:
            self.callback_hash[command_parts[0]](arguments)
