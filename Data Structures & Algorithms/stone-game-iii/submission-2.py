class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            best = float('-inf')

            window = 0
            for j in range(i, min(n, i+3)):
                window += stoneValue[j]
                best = max(best, window - dp[j + 1])
            dp[i] = best
        
        res = dp[0]
        if res == 0:
            return "Tie"
        if res < 0:
            return "Bob"
        return "Alice"