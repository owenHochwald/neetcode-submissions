class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []

        for r in range(k, len(nums)+1):
            window = nums[l:r]
            res.append(max(window))
            l += 1
        return res


        