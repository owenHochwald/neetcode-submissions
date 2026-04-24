"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        times = []
        for i in intervals:
            times.append([i.start, "S"])
            times.append([i.end, "E"])
        
        times.sort()
        count = 0

        for time in times:
            if time[1] == "S":
                count += 1
            if time[1] == "E":
                count -= 1
            
            if count == 2:
                return False

        return True
