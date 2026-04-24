class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack: (index, height)
        stack = []
        maxHeight = 0
        for i, h in enumerate(heights):
            if not stack or stack[-1][1] < h:
                stack.append([i,h])
            # else its not monotonic increasing, we need to change some things
            else:
                farthest_back = i
                while stack and stack[-1][1] >= h:
                    curr_i, curr_h = stack.pop()
                    farthest_back = curr_i
                    # update the maxHeight
                    maxHeight = max(maxHeight, (i - curr_i) * curr_h)
                stack.append([farthest_back,h])

        for i, h in stack:
            maxHeight = max(maxHeight, (len(heights) - i) * h)
        return maxHeight


        