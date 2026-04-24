class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # use a min heap to keep track of the smallest k
        self.heap = [] 
        self.k = k

        # build heap
        for num in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, num)
            elif num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]