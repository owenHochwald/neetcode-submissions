class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 0

        nums = set(nums)

        for num in nums:
            if num-1 not in nums:
                curr_length = 1
                curr = num
                while curr + 1 in nums:
                    curr = curr + 1
                    curr_length += 1
                largest = max(largest, curr_length)
            

        return largest
        