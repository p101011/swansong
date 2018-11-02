class Event:
    def __init__(self, args):
        self.args = args


class DeathEvent(Event):
    def __init__(self, args):
        super().__init__(args)


class ChangeBleeding(Event):
    def __init__(self, args):
        super().__init__(args)

