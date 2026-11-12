
from collections import deque

# Binary Tree - SAYAGO
#
#          S
#         / \
#        A   Y
#       /   / \
#      A   G   O

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    root = Node("S")
    root.left = Node("A")
    root.right = Node("Y")
    root.left.left = Node("A")
    root.right.left = Node("G")
    root.right.right = Node("O")
    return root


def bfs_tree(root):
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


def dfs_tree(root):
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result


if __name__ == "__main__":
    root = build_tree()

    print("=== BINARY TREE ===")
    print("BFS:", " -> ".join(bfs_tree(root)))
    print("DFS:", " -> ".join(dfs_tree(root)))
