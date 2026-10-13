# LAB SHEET 8
# Q2: AVL Tree Rotations

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    if root is None:
        return 0
    return root.height


def balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)


def right_rotate(y):
    x = y.left
    temp = x.right

    x.right = y
    y.left = temp

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    else:
        return root

    root.height = 1 + max(height(root.left),
                          height(root.right))

    bf = balance(root)

    # LL Rotation
    if bf > 1 and data < root.left.data:
        print("LL Rotation")
        return right_rotate(root)

    # RR Rotation
    if bf < -1 and data > root.right.data:
        print("RR Rotation")
        return left_rotate(root)

    # LR Rotation
    if bf > 1 and data > root.left.data:
        print("LR Rotation")
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL Rotation
    if bf < -1 and data < root.right.data:
        print("RL Rotation")
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


root = None

while True:
    print("\n--- AVL TREE ---")
    print("1. Insert")
    print("2. Preorder Traversal")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        data = int(input("Enter Data: "))
        root = insert(root, data)
        print("Node Inserted")

    elif choice == 2:
        print("Preorder Traversal:", end=" ")
        preorder(root)
        print()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")