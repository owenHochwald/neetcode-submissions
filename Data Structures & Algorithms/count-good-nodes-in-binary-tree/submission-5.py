# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def preorder(node, largest_value):
            if not node:
                return

            # logic
            if node.val >= largest_value:
                largest_value = max(largest_value, node.val)
                self.count += 1

            preorder(node.left, largest_value)
            preorder(node.right, largest_value)
            

        preorder(root, float('-inf'))
        return self.count