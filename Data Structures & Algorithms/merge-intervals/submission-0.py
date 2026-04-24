class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        def overlap(b, s):
            front = max(b[0], s[0])
            back = min(b[1], s[1])
            return back - front >= 0

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if overlap(curr, res[-1]):
                # merge
                res[-1] = [min(res[-1][0], curr[0]), max(res[-1][1], curr[1])]
            else:
                res.append(curr)
        
        return res


        