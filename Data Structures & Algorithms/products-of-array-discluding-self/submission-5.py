class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        for i in range(1, len(nums)):
            curr = prefix[i-1] * nums[i-1]
            prefix[i] = curr


        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            curr = suffix[i+1] * nums[i+1]
            suffix[i] = curr

        print(prefix)
        print(suffix)
        out = []

        for i in range(len(nums)):
            out.append(prefix[i] * suffix[i])

        return out