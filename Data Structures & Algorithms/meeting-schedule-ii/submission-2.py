"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])

        res = count = 0
        s = e = 0
        while s < len(start):
            if end[e] > start[s]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
        