class DSAHashEntry:

    def __init__(self, in_key=None, in_value=None):
        # logic if there is no parameters
        if in_key is None:
            self.default_constructor()
        else:
            self.key = in_key
            self.value = in_value
            self.state = 1

    def default_constructor(self):
        self.key = ""
        self.value = None
        self.state = 0

    def set_key(self, in_key):
        self.key = in_key

    def set_value(self, in_value):
        self.value = in_value

    def set_state(self, in_state):
        self.state = in_state

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def get_state(self):
        return self.state
