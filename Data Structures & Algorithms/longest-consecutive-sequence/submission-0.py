class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = {}
        # [lookup[i] = 1 for i in nums]
        for i in nums:
            lookup[i] = 1

        longest = 0

        for num in nums:
            if num - 1 not in lookup:
                curr = 0
                # start our sequence counting
                while num in lookup:
                    curr += 1
                    longest = max(longest, curr)
                    num += 1
        return longest

        