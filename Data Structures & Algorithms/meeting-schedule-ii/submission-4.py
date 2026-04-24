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
        for time in intervals:
            times.append((time.start, "S"))
            times.append((time.end, "E"))
        times.sort()

        count = 0
        overlaps = 0
        for time in times:
            if time[1] == "S":
                count += 1
            if time[1] == "E":
                count -= 1
            overlaps = max(overlaps, count)
        return overlaps
        