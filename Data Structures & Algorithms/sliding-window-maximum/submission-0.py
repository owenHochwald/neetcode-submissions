class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0

        for r in range(k, len(nums)+1):
            subset = nums[l:r]
            subset.sort(reverse=True)
            res.append(subset[0])
            l += 1
        return res
            