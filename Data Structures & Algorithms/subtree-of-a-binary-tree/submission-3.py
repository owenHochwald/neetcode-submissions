# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val == subRoot.val:
                return sameTree(root.right, subRoot.right) and sameTree(root.left, subRoot.left)
            else:
                return False

        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False




    
        