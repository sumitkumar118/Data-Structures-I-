# LAB 10 - Q2: Graph Traversals

from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

n = len(graph)

matrix = [[0] * n for _ in range(n)]

for u in graph:
    for v in graph[u]:
        matrix[u][v] = 1

print("Adjacency Matrix:")
for row in matrix:
    print(row)

print("Adjacency List:", graph)


def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)


def bfs(start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("\nDFS Traversal:")
dfs(0, set())

print("\nBFS Traversal:")
bfs(0)