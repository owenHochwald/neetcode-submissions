class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r= 0 # represents our current window

        while r < len(nums) - 1:
            farthest = 0
            # go through green portion
            for i in range(l, r + 1):
                curr = nums[i]
                farthest = max(farthest, i + curr)
            l = r + 1
            r = farthest
            res += 1
        return res
        