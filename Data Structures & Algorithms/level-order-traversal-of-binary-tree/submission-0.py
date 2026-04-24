# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        if not root:
            return out
        queue = deque()
        queue.append(root)

        while queue:
            length = len(queue)

            entry = []
            for node in range(length):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                entry.append(curr.val)

            out.append(entry)
        
        return out



