class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in nums:
            # make sure we don't double visit elements
            # make sure we only start at the start of a sequence
            curr_length = 0
            element_in_sequence = num
            while element_in_sequence in num_set and element_in_sequence-1 not in num_set:
                curr_length += 1
                num_set.remove(element_in_sequence)
                element_in_sequence += 1

            longest = max(longest, curr_length)



        return longest