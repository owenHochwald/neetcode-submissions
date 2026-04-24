class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        most_water = 0

        while l < r:
            curr_height = min(heights[l], heights[r])
            most_water = max(most_water, (r - l) * curr_height)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return most_water
        