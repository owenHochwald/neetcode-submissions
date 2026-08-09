class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = [] # we will use a min heap

        self.k = k

        for num in nums:
            if len(self.h) < self.k:
                heapq.heappush(self.h, num)
            elif num > self.h[0]:
                heapq.heappushpop(self.h, num)
            
        

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            top = self.h[0]
            if val > top:
                heapq.heappushpop(self.h, val)
        return self.h[0]

        
