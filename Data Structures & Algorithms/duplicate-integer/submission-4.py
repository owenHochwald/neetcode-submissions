from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = defaultdict(list)
        for num in nums:
            if num in unique_set:
                return True
            unique_set[num].append(1)
        return False
            

         