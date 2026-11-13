# Assessment 3.3 - Binary Tree using the name CANONIGO
# Traversals: BFS (level order) and DFS (preorder)

# A node stores one letter, a left child, and a right child
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.left = None
        self.right = None


# ---------- BUILD THE TREE ----------
root = Node("C")                 # root

root.left = Node("A")            # level 1
root.right = Node("N")

root.left.left = Node("O")       # level 2
root.left.right = Node("N")
root.right.left = Node("I")
root.right.right = Node("G")

root.left.left.left = Node("O")  # level 3


# ---------- BFS (uses a queue) ----------
def bfs(root):
    result = []
    queue = [root]                    # start with the root
    while len(queue) > 0:
        current = queue.pop(0)        # take the first node in the queue
        result.append(current.letter) # visit it
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return result


# ---------- DFS (preorder: Root, Left, Right) ----------
def dfs(node, result):
    if node is None:                  # nothing here, go back
        return
    result.append(node.letter)        # visit the node first
    dfs(node.left, result)            # then go all the way left
    dfs(node.right, result)           # then go right


# ---------- RUN ----------
print("BINARY TREE: CANONIGO")
print("Root  :", root.letter)
print("Left  :", root.left.letter)
print("Right :", root.right.letter)
print()

bfs_result = bfs(root)
print("BFS Traversal:", " -> ".join(bfs_result))

dfs_result = []
dfs(root, dfs_result)
print("DFS Traversal:", " -> ".join(dfs_result))
