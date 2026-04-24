class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            curr = (n >> i) & 1
            out = out | curr << (31 - i)
        return out


        