class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # [7,1,7,2,2,4]
        # x.  x
        # x.  x
        # x.  x
        # x.  x     x
        # x.  x     x
        # x.  x x x x
        # x x x x x x
        # gonna store the index, height
        tallest = 0
        stack = []

        for i, h in enumerate(heights):
            furthest_back = i

            while stack and stack[-1][1] > h:
                furthest_back, old_height = stack.pop()
                tallest = max(tallest, (i-furthest_back)*old_height)
                stack
            
            stack.append([furthest_back, h])
        
        print(stack)
        n = len(heights)
        while stack:
            index, height = stack.pop()
            tallest = max(tallest, (n-index)*height)


        return tallest
