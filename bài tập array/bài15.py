class FailFastArrayList:
    def __init__(self):
        self.data = []
        self.modCount = 0

    def add(self, val):
        self.data.append(val)
        self.modCount += 1

    def __iter__(self):
        return self.Iterator(self)

    class Iterator:
        def __init__(self, outer):
            self.outer = outer
            self.cursor = 0
            self.expectedModCount = outer.modCount

        def __iter__(self):
            return self

        def __next__(self):
            if self.expectedModCount != self.outer.modCount:
                raise RuntimeError()
            if self.cursor >= len(self.outer.data):
                raise StopIteration
            val = self.outer.data[self.cursor]
            self.cursor += 1
            return val