# LAB SHEET 6
# Q1: Binary Tree Construction

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)

        if self.root is None:
            self.root = new
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new
                return
            else:
                queue.append(temp.right)

    def display(self):
        if self.root is None:
            print("Tree is Empty")
            return

        queue = [self.root]

        print("Binary Tree (Level Order):")

        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        print()


tree = BinaryTree()

while True:
    print("\n--- BINARY TREE ---")
    print("1. Insert Node")
    print("2. Display Tree")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        data = int(input("Enter Data: "))
        tree.insert(data)
        print("Node Inserted Successfully")

    elif choice == 2:
        tree.display()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")