# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # only need a single node
            # look at left and right (EDGE CASE -> deal with None nodes)
            # swap pos of left and right in the parent and recurse until none

        def swapNodes(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None

            left = swapNodes(node.left)
            right = swapNodes(node.right)
            node.left, node.right = right, left
            return node
        return swapNodes(root)

        