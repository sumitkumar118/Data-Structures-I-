# LAB SHEET 8
# Q1: Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def find_min(root):
    while root.left:
        root = root.left
    return root


def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = None

while True:
    print("\n--- BINARY SEARCH TREE ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display Inorder")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        data = int(input("Enter Data: "))
        root = insert(root, data)
        print("Node Inserted")

    elif choice == 2:
        data = int(input("Enter Data to Delete: "))
        root = delete(root, data)
        print("Deletion Operation Completed")

    elif choice == 3:
        print("Inorder Traversal:", end=" ")
        inorder(root)
        print()

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")