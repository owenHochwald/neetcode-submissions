class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = float('inf')
        for p in prices:
            l = min(l, p)
            best = max(best, p - l)

        return best