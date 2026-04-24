class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        # build the prefix array
        prefix = [1] * len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        # build the postfix array
        postfix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        # building output array
        for i in range(len(nums)):
            out.append(prefix[i] * postfix[i])
        print(prefix)
        print(postfix)
        return out
        