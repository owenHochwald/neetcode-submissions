class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        for i in range(len(nums)):
            total = 1
            for n in range(len(nums)):
                if n != i:
                    total *= nums[n]
            out.append(total)
        return out
        