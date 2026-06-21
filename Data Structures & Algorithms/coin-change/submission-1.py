class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}

        def dfs(curr):
            if curr < 0:
                return float('inf')
            if curr == 0:
                return 0
            
            if curr not in memo:
                attempts = float('inf')

                for c in coins:
                    if amount - curr >= 0:
                        attempts = min(attempts, dfs(curr- c)+1)
                memo[curr] = attempts
            
            
            return memo[curr]


        out = dfs(amount)
        return out if out != float('inf') else -1
        