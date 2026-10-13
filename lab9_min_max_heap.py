# LAB SHEET 9
# Q1: Min Heap and Max Heap

class Heap:
    def __init__(self, is_min=True):
        self.heap = []
        self.is_min = is_min

    def compare(self, a, b):
        if self.is_min:
            return a < b
        return a > b

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        # Bubble Up
        while i > 0:
            parent = (i - 1) // 2

            if self.compare(self.heap[i], self.heap[parent]):
                self.heap[i], self.heap[parent] = (
                    self.heap[parent], self.heap[i]
                )
                i = parent
            else:
                break

    def delete_root(self):
        if not self.heap:
            print("Heap is Empty")
            return

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            i = 0
            n = len(self.heap)

            # Bubble Down
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                best = i

                if left < n and self.compare(
                    self.heap[left], self.heap[best]
                ):
                    best = left

                if right < n and self.compare(
                    self.heap[right], self.heap[best]
                ):
                    best = right

                if best == i:
                    break

                self.heap[i], self.heap[best] = (
                    self.heap[best], self.heap[i]
                )
                i = best

        print("Deleted Root:", root)

    def display(self):
        print("Heap:", self.heap)


min_heap = Heap(True)
max_heap = Heap(False)

while True:
    print("\n--- MIN AND MAX HEAP ---")
    print("1. Insert")
    print("2. Delete Root")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 4:
        print("Program Ended")
        break

    print("1. Min Heap")
    print("2. Max Heap")
    type_choice = int(input("Choose Heap: "))

    if type_choice == 1:
        h = min_heap
    elif type_choice == 2:
        h = max_heap
    else:
        print("Invalid Heap Choice")
        continue

    if choice == 1:
        value = int(input("Enter Value: "))
        h.insert(value)
        print("Element Inserted")

    elif choice == 2:
        h.delete_root()

    elif choice == 3:
        h.display()

    else:
        print("Invalid Choice")