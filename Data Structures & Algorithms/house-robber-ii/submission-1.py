class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        s1 = nums[:-1]
        s2 = nums[1:]
        
        def rob_range(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]

            memo = {0:houses[0], 1: max(houses[0], houses[1])}

            def dfs(n):
                if n not in memo:
                    memo[n] = max(houses[n] + dfs(n - 2), dfs(n - 1))
                return memo[n]  
            
            return dfs(len(houses) - 1)
        
        return max(rob_range(s1), rob_range(s2))
