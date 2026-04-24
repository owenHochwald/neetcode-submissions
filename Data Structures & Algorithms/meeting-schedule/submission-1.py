"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x : x.start)

        def overlap(i, p):
            front = max(i.start, p.start)
            back = min(i.end, p.end)
            return back - front > 0
        
        baseline = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if overlap(baseline, curr):
                return False
            baseline = curr
        return True

