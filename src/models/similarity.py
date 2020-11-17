class Similarity:
    def __init__(self, weight):
        self.weight = weight

    def params_str(self):
        return "{{weight: {}}}".format(self.weight)
