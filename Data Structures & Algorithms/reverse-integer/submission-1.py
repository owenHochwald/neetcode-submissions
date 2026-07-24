class Solution:
    def reverse(self, x: int) -> int:
        # reverse the digits
        # check if it will be outside of the range
            # niche binary stuff

        rev = int(str(abs(x))[::-1])
        if x < 0:
            rev = -rev

        if -(2 ** 31 )<= -rev <=( 2 ** 31 )-1:
            return rev
        return 0