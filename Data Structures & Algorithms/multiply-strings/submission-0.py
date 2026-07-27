class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def convert(item) -> int:
            x = 0
            for c in item:
                x *= 10
                x += int(c)
            return x




        return str(convert(num1) * convert(num2))
        