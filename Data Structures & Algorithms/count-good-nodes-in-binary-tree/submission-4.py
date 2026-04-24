# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def preorder(node, top):
            nonlocal count
            if not node:
                return
            else:
                if node.val >= top:
                    count += 1
                curr = max(top, node.val)
                preorder(node.left, curr)
                preorder(node.right, curr)

        preorder(root, float('-inf'))
        return count