class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        rc, wc, bc, = 0, 0, 0

        for c in nums:
            if c == 0:
                rc += 1
            elif c == 1:
                wc += 1
            else:
                bc += 1
        
        for i in range(len(nums)):
            if rc > 0:
                nums[i] = 0
                rc -= 1
            elif wc > 0:
                nums[i] = 1
                wc -= 1
            else:
                nums[i] = 2
                bc -= 1
        