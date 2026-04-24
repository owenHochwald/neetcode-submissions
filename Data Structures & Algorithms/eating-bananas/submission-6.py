class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        smallest = r

        def ableToEat(num):
            count = 0
            for pile in piles:
                count += math.ceil(pile / num )
                print(count)
            return count <= h


        while l < r:
            m = (r+l) // 2
            if ableToEat(m):
                smallest = m
                r = m
            else:
                l = m + 1
        return smallest

        
        