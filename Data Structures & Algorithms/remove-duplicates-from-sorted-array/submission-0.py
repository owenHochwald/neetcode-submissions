class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        written = -101

        for i, read in enumerate(nums): 
            if read != written:
                written = read
                nums[write] = read
                write += 1
        return write 





