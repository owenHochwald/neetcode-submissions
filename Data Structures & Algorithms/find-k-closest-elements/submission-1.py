class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def calculate_diff(a):
            return abs(a-x)

        nums = [[calculate_diff(a), a] for a in arr]
        nums.sort() # sort according to the min diff
        print(nums)
        return sorted([x[1] for x in nums[:k]])
