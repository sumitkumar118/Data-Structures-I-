# LAB SHEET 6
# Q2: Binary Tree Traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive Inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Recursive Preorder
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Recursive Postorder
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Iterative Inorder
def iterative_inorder(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")
        current = current.right


# Iterative Preorder
def iterative_preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data, end=" ")

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


# Iterative Postorder
def iterative_postorder(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    while stack2:
        print(stack2.pop().data, end=" ")


# Creating Binary Tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Recursive Inorder:")
inorder(root)

print("\nRecursive Preorder:")
preorder(root)

print("\nRecursive Postorder:")
postorder(root)

print("\n\nIterative Inorder:")
iterative_inorder(root)

print("\nIterative Preorder:")
iterative_preorder(root)

print("\nIterative Postorder:")
iterative_postorder(root)

print()