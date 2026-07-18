import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # note that we want to have our heap only have things that we CAN afford
            # that way we pick the thing with the most profi
        # but in order to reasonably figure out if we can afford something
        # we want to make sure that we have all of our capital things sorted
            # but if we afford something we should add it to the heap
            # which means that we need to zip profits and capital        
        pointer = 0
        afford = sorted(list(zip(capital, profits)))
        heap = []


        # while k > 0 and w >= afford[pointer][0]:
        while k > 0:
            while pointer < len(afford) and w >= afford[pointer][0]:
                heapq.heappush(heap, -afford[pointer][1])
                pointer += 1

            if not heap:
                return w 
            w += -heapq.heappop(heap)
            k -= 1

        return w

            
