# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # at each step you can either
        # take the current node
        # or skip the node
        # greedy doesn't work because you can fall into a situation where you should've skipped only looking 1 ahead
        # if i take this level in the branch, I can't take the next level


        # returns [rob_this, skip_this]
        def dfs(curr):
            if not curr:
                return [0, 0]
                
            left_rob, left_skip = dfs(curr.left)
            right_rob, right_skip = dfs(curr.right)
            rob_this = curr.val + left_skip + right_skip
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)

            return [rob_this, skip_this]

        rob_this, skip_this = dfs(root) 
        return max(rob_this, skip_this)