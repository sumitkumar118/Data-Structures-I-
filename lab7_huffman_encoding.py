# LAB SHEET 7
# Q1: Huffman Encoding

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def generate_codes(root, code=""):
    if root is None:
        return

    if root.char is not None:
        print(root.char, ":", code or "0")
        return

    generate_codes(root.left, code + "0")
    generate_codes(root.right, code + "1")

def huffman_encoding(chars, freq):
    heap = []
    count = 0

    for i in range(len(chars)):
        node = Node(chars[i], freq[i])
        heapq.heappush(heap, (freq[i], count, node))
        count += 1

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        new = Node(None, f1 + f2)
        new.left = left
        new.right = right

        heapq.heappush(heap, (new.freq, count, new))
        count += 1

    if heap:
        root = heapq.heappop(heap)[2]
        print("\nHuffman Codes:")
        generate_codes(root)

n = int(input("Enter number of characters: "))

chars = []
freq = []

for i in range(n):
    ch = input("Enter character: ")
    f = int(input("Enter frequency: "))

    chars.append(ch)
    freq.append(f)

huffman_encoding(chars, freq)