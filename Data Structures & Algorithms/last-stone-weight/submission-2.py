import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            smash = abs(first)-abs(second)
            # if smash > 0:
            heapq.heappush(heap, -smash)


        return abs(heap[0])