"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = {}
        stack = [node]

        nodes[node] = Node(node.val)

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in nodes:
                    clone = Node(neighbor.val)
                    nodes[neighbor] = clone 
                    stack.append(neighbor)
                nodes[curr].neighbors.append(nodes[neighbor])

        return nodes[node]


        