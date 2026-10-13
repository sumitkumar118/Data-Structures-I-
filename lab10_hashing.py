# LAB 10 - Q1: Hashing

class OpenHash:
    def __init__(self, size=5):
        self.table = [[] for _ in range(size)]

    def insert(self, key):
        index = key % len(self.table)
        self.table[index].append(key)

    def display(self):
        print("Open Hashing:", self.table)


class ClosedHash:
    def __init__(self, size=5):
        self.table = [None] * size
        self.count = 0

    def insert(self, key):
        if (self.count + 1) / len(self.table) > 0.7:
            self.rehash()

        index = key % len(self.table)

        while self.table[index] is not None:
            index = (index + 1) % len(self.table)

        self.table[index] = key
        self.count += 1

    def rehash(self):
        old = self.table
        self.table = [None] * (len(old) * 2)
        self.count = 0

        for key in old:
            if key is not None:
                self.insert(key)

    def display(self):
        print("Closed Hashing:", self.table)


a = OpenHash()
b = ClosedHash()

for x in [10, 15, 20, 25]:
    a.insert(x)
    b.insert(x)

a.display()
b.display()