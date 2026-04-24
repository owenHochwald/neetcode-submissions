class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32 bits of 1s
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # If a is negative in 32-bit representation
        return a if a <= MAX_INT else ~(a ^ MASK)
