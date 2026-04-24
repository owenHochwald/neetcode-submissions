class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
 
            m = (l+r) // 2
            left = nums[m-1] if m-1 >= 0 else float('inf')
            right = nums[m+1] if m+1 < n else float('inf')

            if nums[m] == target:
                return m
            # if left < target <= right:
            #     return m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1

        return l

        