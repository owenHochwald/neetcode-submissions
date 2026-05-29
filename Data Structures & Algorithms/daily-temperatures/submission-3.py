class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n 

        s = []

        for i in range(n-1, -1, -1):
            curr = temperatures[i]

            while s and curr >= s[-1][1]:
                s.pop()
            
            if s:
                out[i] = s[-1][0] - i
            s.append([i, curr])

        


        return out