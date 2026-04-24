class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, math.ceil(x/2)

        while l <= r:
            m = (l+r) // 2
            
            # if m * m == x or (m-1) * (m-1) < x < (m+1) * (m+1):
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        return r

        