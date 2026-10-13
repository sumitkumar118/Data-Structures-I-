# LAB ASSIGNMENT 4
# Q4: Queue Using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new = Node(data)

        if self.rear is None:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new

        print("Element Inserted:", data)

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        print("Element Deleted:", self.front.data)
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front
        print("Queue:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


q = Queue()

while True:
    print("\n--- QUEUE USING LINKED LIST ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        value = int(input("Enter Value: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
        