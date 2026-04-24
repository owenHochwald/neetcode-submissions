class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lookup = {}
        for i, c in enumerate(s):
            if c not in lookup:
                lookup[c] = [i, i]
            else:
                lookup[c][1] = i

        intervals = list(lookup.values())
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for start, end in intervals[1:]:
            last_start, last_end = res[-1]
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return [end - start + 1 for start, end in res]
