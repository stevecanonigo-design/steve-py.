# Assessment 3.3 - Graph using the unique letters of CANONIGO: C, A, N, O, I, G
# Traversals: BFS and DFS, starting at vertex C

# Adjacency list: each vertex lists the vertices it is connected to
graph = {
    "C": ["A", "N"],
    "A": ["C", "N", "O"],
    "N": ["C", "A", "I"],
    "O": ["A", "G"],
    "I": ["N", "G"],
    "G": ["O", "I"]
}


# ---------- BFS (uses a queue) ----------
def bfs(graph, start):
    visited = [start]                 # vertices already visited
    queue = [start]                   # vertices waiting to be processed
    while len(queue) > 0:
        current = queue.pop(0)        # take the first vertex
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


# ---------- DFS (uses recursion) ----------
def dfs(graph, vertex, visited):
    visited.append(vertex)            # mark the vertex as visited
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # go deeper first
    return visited


# ---------- RUN ----------
print("GRAPH: C, A, N, O, I, G")
print("Adjacency List:")
for vertex in graph:
    print(" ", vertex, "->", ", ".join(graph[vertex]))
print()

print("Starting Vertex: C")
print("BFS Traversal:", " -> ".join(bfs(graph, "C")))
print("DFS Traversal:", " -> ".join(dfs(graph, "C", [])))
