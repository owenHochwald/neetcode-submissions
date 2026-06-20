import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # we need to track letter counts
        # we need to track the previous character length
        # how do we track the substring constraint?
        # prev_freq, prev_ch
        # we go to insert another because ch == prev_ch and ch is most frequent
        # but we skip it because prev_freq = 2
        heap = []
        if a > 0:
            heap.append([-a, 'a'])
        if b > 0:
            heap.append([-b, 'b'])
        if c > 0:
            heap.append([-c, 'c'])
        heapq.heapify(heap)

        out = []

        while heap:
            freq, ch = heapq.heappop(heap)
            
            if len(out) >= 2 and out[-2] == out[-1] == ch:
                # if we're gonna violate the constraint, try poping the next element
                if not heap:
                    break
                else:
                    new_freq, new_ch = heapq.heappop(heap)
                    heapq.heappush(heap, [freq, ch])
                    freq, ch = new_freq, new_ch

            out.append(ch)
            freq += 1
            if freq < 0:
                heapq.heappush(heap, [freq, ch])

        return ''.join(out)

        