class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1:[0,3]
        # 2:[1]
        # 3:[2]
        
        # 2:[0,2]
        # 1:[1]

        lookup = defaultdict(list)

        for i, num in enumerate(nums):
            if len(lookup[num]) > 0:

                for j in lookup[num]:
                    if abs(i-j) <= k:
                        return True


            lookup[num].append(i)

        return False


            


        