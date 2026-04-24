class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.done = False
        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        if total % 4 != 0:
            return self.done
        target = total / 4

        def backtrack(i, top, bot, left, right):
            if self.done:
                return
            if i >= len(matchsticks):
                cond = (top == bot == left == right)
                self.done = self.done or cond
                return
            # checking target length condition
            if top > target or bot > target or left > target or right > target:
                return
            # backtracking logic
            curr = matchsticks[i]
            backtrack(i+1, top + curr, bot, left, right)
            backtrack(i+1, top, bot + curr, left, right)
            backtrack(i+1, top, bot, left + curr, right)
            backtrack(i+1, top, bot, left, right + curr)
            



        backtrack(0, 0, 0, 0, 0)
        return self.done
        