# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        # easy way to do this with post order

        def dfs(node):
            if not node:
                return

            # post order
            dfs(node.left)
            dfs(node.right)

            if is_leaf(node.left) and node.left.val == target:
                node.left = None

            if is_leaf(node.right) and node.right.val == target:
                node.right = None

            
            
        
        dfs(root)
        return root if (root and root.val != target) else None