class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]]
        for i in range(1, len(height)):
            prefix.append(max(prefix[i-1], height[i]))

        suffix = [0] * len(height)
        suffix[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])

        total = 0

        for i in range(len(height)):
            total += max(0, min(suffix[i], prefix[i]) - height[i])
        return total
        