"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = None
        nodes = {}

        while head:
            curr = Node(head.val)
            if not res:
                res = curr
            nodes[head] = curr
            head = head.next

        for key in nodes.keys():
            newNode = nodes[key]
            if key.next:
                newNode.next = nodes[key.next]
            if key.random:
                newNode.random = nodes[key.random]

        return res

        