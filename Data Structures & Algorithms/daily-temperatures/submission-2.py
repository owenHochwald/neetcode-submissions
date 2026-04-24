class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # temperatures = [30,38,30,36,35,40,28]
        #                                 1, 4,1,2,1,0,0
        #                                     [(38, 1), (40, 6)]
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)-1, -1, -1):
            curr = temperatures[i]

            while stack and stack[-1][0] <= curr:
                stack.pop()

            if stack:
                res[i] = stack[-1][1] - i
            stack.append([curr, i])
            


        return res

        