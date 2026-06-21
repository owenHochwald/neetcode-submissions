class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount+1)

        for i in range(1, amount + 1):
            num_used = float('inf')

            for c in coins:
                if i - c >= 0:
                    num_used = min(num_used, dp[i-c] + 1)
            dp[i] = num_used

        print(dp)

        return dp[amount] if dp[amount] != float('inf') else -1

        
