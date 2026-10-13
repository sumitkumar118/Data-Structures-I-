# LAB ASSIGNMENT 3
# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_tail(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    def insert_position(self, data, pos):
        if pos < 0:
            print("Invalid Position")
            return

        if pos == 0:
            self.insert_head(data)
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new = Node(data)
        new.next = temp.next
        temp.next = new

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            print("Node Deleted")
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Node Not Found")
            return

        prev.next = temp.next
        print("Node Deleted")

    def display(self):
        temp = self.head

        if temp is None:
            print("List is Empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


sll = SinglyLinkedList()

while True:
    print("\n--- SINGLY LINKED LIST ---")
    print("1. Insert at Head")
    print("2. Insert at Tail")
    print("3. Insert at Position")
    print("4. Delete Node")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        data = int(input("Enter Data: "))
        sll.insert_head(data)

    elif choice == 2:
        data = int(input("Enter Data: "))
        sll.insert_tail(data)

    elif choice == 3:
        data = int(input("Enter Data: "))
        pos = int(input("Enter Index: "))
        sll.insert_position(data, pos)

    elif choice == 4:
        key = int(input("Enter Data to Delete: "))
        sll.delete(key)

    elif choice == 5:
        sll.display()

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")