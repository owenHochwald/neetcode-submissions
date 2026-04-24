# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]
        
        # return max path sum without splitting
        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # max with split
            res[0] = max(res[0], node.val + left + right)
            # return without split
            return node.val + max(left, right)

        dfs(root)
        return res[0]

