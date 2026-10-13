# LAB SHEET 8
# Q3: B-Tree of Order 3

class Node:
    def __init__(self):
        self.keys = []
        self.children = []


class BTree:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        result = self.insert_node(self.root, key)

        if result is not None:
            middle, right = result

            new_root = Node()
            new_root.keys = [middle]
            new_root.children = [self.root, right]

            self.root = new_root

    def insert_node(self, node, key):
        if key in node.keys:
            return None

        if not node.children:
            node.keys.append(key)
            node.keys.sort()

        else:
            i = 0

            while i < len(node.keys) and key > node.keys[i]:
                i += 1

            result = self.insert_node(node.children[i], key)

            if result is not None:
                middle, right = result

                node.keys.insert(i, middle)
                node.children.insert(i + 1, right)

        if len(node.keys) <= 2:
            return None

        middle = node.keys[1]

        right = Node()
        right.keys = node.keys[2:]

        if node.children:
            right.children = node.children[2:]
            node.children = node.children[:2]

        node.keys = node.keys[:1]

        print("Node Split at:", middle)

        return middle, right

    def display(self, node=None, level=0):
        if node is None:
            node = self.root

        print("Level", level, ":", node.keys)

        for child in node.children:
            self.display(child, level + 1)


btree = BTree()

while True:
    print("\n--- B-TREE ORDER 3 ---")
    print("1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        data = int(input("Enter Data: "))
        btree.insert(data)
        print("Insertion Completed")

    elif choice == 2:
        btree.display()

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")