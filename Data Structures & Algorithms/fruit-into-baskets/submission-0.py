class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # only have two baskets, a basket can only have 1 type of fruit
        # only only select two types of fruit, unlimited amount

        # the starting point for when we choose to pick from matters!
        # this is sort of a sliding window problem

        # EXAMPLES
        # if we choose to expand from 
        # 0, 1, which means that when we get to 2, we have to start drop
            # what is the shrink condition?
                # when we have 3 types of fruit, more than 2
            # what do we do?
                # pop from the left until we only have 1 type
        
            # how do we keep track of max,
                # take the max for each time we add while it is still valid

        mx = 0
        l, n = 0, len(fruits)
        c = defaultdict(int)
        for r, f in enumerate(fruits):
            c[f] += 1
            while c and len(c) > 2:
                c[fruits[l]] -= 1
                if not c[fruits[l]]:
                    del c[fruits[l]]
                l += 1
            curr = sum(c.values())
            mx = max(mx, curr)
        return mx





        return mx