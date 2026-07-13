import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        
        heap = []
        curr = 0

        for num, f, t in trips:
            while heap and heap[0][0] <= f:
                dropoff, passen = heapq.heappop(heap)
                curr -= passen

            curr += num
            if curr > capacity:
                return False
            heapq.heappush(heap, (t, num))
        return True