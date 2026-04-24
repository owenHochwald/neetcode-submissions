class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        for i in range(32):
            bit = (n >> i) & 1
            out += bit
        return out

        