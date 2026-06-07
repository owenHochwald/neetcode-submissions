class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best, curr = len(nums) + 1, 0
        l = 0

        for r, num in enumerate(nums):
            curr += num
            # might have a problem with l < r
            while curr >= target and l <= r:
                best = min(best, r - l + 1)
                curr -= nums[l]
                l += 1

        return 0 if best == len(nums) + 1 else best
        