class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if total % 2 != 0:
            return False
        target = total // 2


        memo = {0:0}
        def can_sum(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]
            if curr == 0:
                return True
            if i == len(nums):
                return False
            take = can_sum(i+1, curr-nums[i])
            skip = can_sum(i+1, curr)
            memo[(i, curr)] = take or skip
            return memo[(i, curr)]

            

        return can_sum(0, target)

        


        