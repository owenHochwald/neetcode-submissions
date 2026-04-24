class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = set()

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    out.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr > 0:
                    r -= 1
                else:
                    l += 1
        return list(out)
                
        