class ArrayListEndOps:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def popBack(self):
        if self.data:
            return self.data.pop()
        return None