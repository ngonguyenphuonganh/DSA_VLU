class ArrayListInsertRemove:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def remove(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        raise IndexError()