class OnlineSort:
    def __init__(self):
        self.a = []
    
    def add_element(self, x):
        self.a.append(x)
        i = len(self.a) - 1
        while i > 0 and self.a[i - 1] > self.a[i]:
            self.a[i], self.a[i - 1] = self.a[i - 1], self.a[i]
            i -= 1
        return self.a

online = OnlineSort()
for x in [5, 2, 8, 1]:
    print(online.add_element(x))