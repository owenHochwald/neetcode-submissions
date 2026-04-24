class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # can't select more weight than the ship can hold
        # each day we can make a trip with the max weight from the ship
        # each day might have a different capacity
        # we want to return the max, least-capacity day that still allows us to ship everything

        # lower bound for our answer is the max in the list
        # upper bound for our answer is sum(weights)

        # case 1, len(weights) == days
            # answer is the max(weights)

        # case 2, len(weights) < days
            # answer is still max(weights) -> weights are atomic

        # case 3, len(weights) > days
            # we can make combinations, but we never want to take more than the max
                # might happen -> [1,2,3,4,4,5] -> 3 days

        # we don't get to change the order of the weights!
        # each step we have to take at least 1 item...
        # then do we take or exclude the next one?
        l, r = max(weights), sum(weights)
        res = r

        def works(val):
            ships, curr = 1, val
            for w in weights:
                if curr - w < 0:
                    # make a fresh ship if we can't
                    ships += 1
                    curr = val
                
                curr -= w
            return ships <= days





        while l <= r:
            m = (l+r) // 2

            if works(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res

        