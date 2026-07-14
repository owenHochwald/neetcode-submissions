class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # helper that tells us if something is a or b is closer 

        # x is not in arr so what do we do?


        # grow window on each side (picking between left or right) until we have k elements 
        # while loop

        # edge cases:
        # x all x the way on the right
            # if trying to access a or b is out of bounds, just set the thing to negative inf


        # what if we create a new array of the difference values [diff, num] 
            # then we adjust to all be positive
            # take the top k after resorting!


        def calculate_diff(a):
            return abs(a-x)

        nums = [[calculate_diff(a), a] for a in arr]
        nums.sort() # sort according to the min diff
        print(nums)
        return sorted([x[1] for x in nums[:k]])




        # return the sorted(nums)




