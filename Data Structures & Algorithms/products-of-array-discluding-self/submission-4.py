class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_rtl = [1, 1, 2, 8]
        # prefix_ltf = [48, 24, 6, 1]

        # this works because at each step we're getting the sum of the left hand side without this part
        # and also the right hand side without this part

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        out = []
        for i in range(n):
            product_except_self = prefix[i] * suffix[i]
            out.append(product_except_self)
        return out