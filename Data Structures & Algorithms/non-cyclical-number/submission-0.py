class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            digits = [int(i) * int(i)  for i in str(n)]
            n = sum(digits)

        
        return True
        