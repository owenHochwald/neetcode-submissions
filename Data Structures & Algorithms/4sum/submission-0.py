class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # TRICK -> add indeces not vals -> map to vals at the end
        out = set() # need ALL UNIQUE -> not just first -> should add to set in ascend order
        n = len(nums)
        if n < 4: return []

        # generate all pairs -> O(n^2)
        pairs = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                # ensure sorted
                pairs[nums[i] + nums[j]].append((i, j))
        
        for i in range(n):
            for j in range(i+1, n):
                curr = nums[i] + nums[j]
                need = target - curr

                if need in pairs:
                    # for all of the pairs with this matched sum
                    for x, y in pairs[need]:
                        if j < x: # each pair is garn. to be sorted -> check that pairs are incres

                            to_add = tuple(sorted([nums[i], nums[j], nums[x], nums[y]]))
                            out.add(to_add)

        return [list(s) for s in out]



        

