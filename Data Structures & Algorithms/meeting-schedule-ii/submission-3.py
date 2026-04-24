"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for i in intervals:
            times.append([i.start, "S"])
            times.append([i.end, "E"])

        times.sort()
        count = 0
        res = 0

        for time in times:
            if time[1] == "S":
                count += 1
            if time[1] == "E":
                count -= 1
            res = max(res, count)

        return res
        
