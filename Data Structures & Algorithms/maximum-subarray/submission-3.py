class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        curr = 0

        for num in nums:
            curr += num

            max_sum = max(max_sum, curr)


            if curr < 0:
                curr = 0
            
        
        return max_sum
        