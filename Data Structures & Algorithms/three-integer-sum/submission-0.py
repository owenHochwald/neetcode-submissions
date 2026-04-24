class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []

        nums = sorted(nums)
        for i in range(len(nums)):
            # now run the two sum sorted two pointer approch
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr = nums[l] + nums[r]
                if curr == -nums[i]:
                    if sorted([nums[l], nums[r], nums[i]]) not in out:
                        out.append(sorted([nums[l], nums[r], nums[i]]))
                    l += 1
                elif curr > -nums[i]:
                    r -= 1
                else:
                    l += 1
        return out


            

        return out
        