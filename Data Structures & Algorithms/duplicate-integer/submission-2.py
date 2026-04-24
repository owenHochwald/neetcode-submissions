class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if len(nums) <= 1:
            return False
        def handleRec(prev, nums):
            if len(nums) == 0:
                return False
            elif prev == nums[0]:
                return True
            else:
                return handleRec(nums[0], nums[1:])
        return handleRec(nums[0], nums[1:])
            

         