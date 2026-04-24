class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for d in digits:
            number *= 10
            number += d
        print(number)

        number += 1
        res = [int(i) for i in str(number)]
        return res