class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # [3,4,4,5,6,1,2,2]
        # l = 0, r = 7

        # 5
        # if l < target < m:
        #     search in that path   
        # elif r < target < mid
        
        
        # 3, 2

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            left, right, mid = nums[l], nums[r], nums[m]

            if left == target or right == target or mid == target:
                return True
            if left < mid:
                if left < target < mid:
                    r = m
                else:
                    l = m + 1
            elif mid < right:
                if mid < target < right:
                    l = m + 1
                else: 
                    r = m
            if mid == left:
                l += 1
            if mid == right:
                r -= 1 


        return False 
