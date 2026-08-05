# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # 1 or 0 handling
                # if their both no children we can just return None -> boils up
                # else it will just get the other one which is satisfying
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            succ = root.right
            while succ.left:
                succ = succ.left
            
            root.val = succ.val
            # the bubbling up, we gotta delete the node we just swapped with
            root.right = self.deleteNode(root.right, succ.val)
        return root
                

