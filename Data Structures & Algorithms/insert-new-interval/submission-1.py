class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            # if newInterval is less than the first one
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(intervals[i])
                # don't append new interval since it could conflict
            else:
                # it overlaps so we merge
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                # don't add to result because it could be overlapping
        res.append(newInterval)
        return res
        