class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        res = [intervals[0]]
        overlaps = 1

        def overlap(b, s):
            front = max(b[0], s[0])
            back = min(b[1], s[1])
            return back - front > 0
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if not overlap(res[-1], curr):
                res[-1] = curr
                overlaps += 1
        
        return len(intervals) - overlaps
        