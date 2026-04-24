class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mostWater = 0

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            mostWater = max(mostWater, curr)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return mostWater


        