class Listened:
    def __init__(self, times):
        self.times = times

    def params_str(self):
        return "{{times: '{}'}}".format(self.times)
