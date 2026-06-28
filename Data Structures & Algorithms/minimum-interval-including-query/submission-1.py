class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        out = []
        # sort by start time
        intervals.sort()


        # for each query
        for q in queries:
            # while the start time is less than or equal to query
            i = 0
            heap = []
            while i < len(intervals) and intervals[i][0] <= q:
                    # exclude those with later ending times
                s_i, e_i = intervals[i]
                i += 1
                if e_i < q:
                    continue 
                # insert to a min heap
                length = e_i - s_i + 1
                heapq.heappush(heap, length)
            # pop the one from the min heap
            val = heapq.heappop(heap) if heap else -1
            out.append(val)
        return out