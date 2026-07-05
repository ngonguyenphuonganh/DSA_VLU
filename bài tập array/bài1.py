class ArrayListBasic:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError()

    def set(self, index, value):
        if 0 <= index < len(self.data):
            self.data[index] = value
        else:
            raise IndexError()

    def size(self):
        return len(self.data)