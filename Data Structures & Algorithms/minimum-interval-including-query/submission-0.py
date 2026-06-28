class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        out = [0] * len(queries)

        lookup = {}


        for s, e in intervals:
            length = e - s + 1
            for num in range(s, e+1):
                lookup[num] = min(lookup.get(num, float('inf')), length)

        for i, q in enumerate(queries):
            out[i] = lookup.get(q, -1)





        return out
        