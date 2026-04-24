import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        # build normal array and heapify
        heap = [-val for val in freqs.values()]
        heapq.heapify(heap)

        time = 0
        cooldown = deque()

        while heap or cooldown:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    cooldown.append((cnt, time + n))

            if cooldown and cooldown[0][1] <= time:
                heapq.heappush(heap, cooldown.popleft()[0])
            
        return time

        