# LAB 10 - Q3: Minimum Spanning Tree

import heapq

edges = [
    (1, 0, 1),
    (4, 0, 2),
    (2, 1, 2),
    (5, 1, 3),
    (3, 2, 3)
]

n = 4

# Kruskal's Algorithm
parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

cost = 0
print("Kruskal MST:")

for w, u, v in sorted(edges):
    a, b = find(u), find(v)

    if a != b:
        parent[a] = b
        cost += w
        print(u, "-", v, ":", w)

print("Total Cost:", cost)


# Prim's Algorithm
graph = [[] for _ in range(n)]

for w, u, v in edges:
    graph[u].append((w, v))
    graph[v].append((w, u))

visited = set()
heap = [(0, 0, -1)]
cost = 0

print("\nPrim MST:")

while heap:
    w, u, p = heapq.heappop(heap)

    if u in visited:
        continue

    visited.add(u)
    cost += w

    if p != -1:
        print(p, "-", u, ":", w)

    for weight, v in graph[u]:
        if v not in visited:
            heapq.heappush(heap, (weight, v, u))

print("Total Cost:", cost)