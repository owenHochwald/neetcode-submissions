class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.num = x


        if n < 0:
            self.num = 1 / x
            n = -n
        def dfs(i) -> float:
            if i == 0:
                return 1

            half = dfs(i // 2)
            if i % 2 == 0:
                return half * half
            return half * half * self.num

        return dfs(n)