# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lookup = {val: idx for idx, val in enumerate(inorder)}

        def divide(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r or in_l > in_r:
                return None
            else:
                node = TreeNode(preorder[pre_l])
                index = lookup[preorder[pre_l]]

                leftSize = index - in_l
                rightSize = len(preorder) - leftSize 

                node.left = divide(pre_l + 1, pre_l + leftSize, in_l, index-1)
                node.right = divide(pre_l + leftSize +1, pre_r, index+1, in_r)

                return node

        root = divide(0, len(preorder)-1, 0, len(inorder))
        return root

        