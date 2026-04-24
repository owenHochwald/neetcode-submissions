import heapq
class MedianFinder:

    def __init__(self):
        self.lower = [] # max heap
        self.upper = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)

        if self.upper and self.lower and (-self.lower[0] > self.upper[0]):
            # optimistically add to left

            # pop from lower and add to upper to account for slip ups
            heapq.heappush(self.upper, -heapq.heappop(self.lower))

        # rebalance the lens
        if len(self.upper) - len(self.lower) > 1:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
        
        elif len(self.lower) - len(self.upper) > 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]  # This was missing!
        else:
            return (-self.lower[0] + self.upper[0]) / 2




        
        