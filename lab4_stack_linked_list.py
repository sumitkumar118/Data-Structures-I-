# LAB ASSIGNMENT 4
# Q2: Stack Using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new
        print("Element Pushed:", data)

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Element Popped:", self.top.data)
            self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Stack is Empty")
            return

        temp = self.top
        print("Stack (Top to Bottom):")

        while temp:
            print(temp.data)
            temp = temp.next


s = Stack()

while True:
    print("\n--- STACK USING LINKED LIST ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        value = int(input("Enter Value: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")