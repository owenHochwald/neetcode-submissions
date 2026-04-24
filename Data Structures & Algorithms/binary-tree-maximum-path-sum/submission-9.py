# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.total = root.val

        def helper(node):
            if not node:
                return 0
            
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            self.total = max(self.total, node.val + left + right)

            return max(node.val + left, node.val + right)



        helper(root)
        return self.total