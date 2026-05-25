class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # get rid of all occurences of val
            # what if we allocate n (where n is number of val)
            # to the back of nums, then swap everything over

        # we can use a two pointer approach where we have
        # and track a starting good pointer that we 
        # move elements to, and the one that traverses
        # and discovers bad ones

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

            