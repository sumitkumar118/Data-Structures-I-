# LAB SHEET 7
# Q2: Optimal Merge Pattern

import heapq

def optimal_merge(files):
    heapq.heapify(files)

    total_cost = 0

    print("\nOptimal Merge Sequence:")

    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)

        merge_cost = first + second

        print(first, "+", second, "=", merge_cost)

        total_cost += merge_cost

        heapq.heappush(files, merge_cost)

    return total_cost


n = int(input("Enter number of files: "))

files = []

for i in range(n):
    size = int(input("Enter file size: "))
    files.append(size)

result = optimal_merge(files)

print("\nMinimum Total Merge Cost:", result)
