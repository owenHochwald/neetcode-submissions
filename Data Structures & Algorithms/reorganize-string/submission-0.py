from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # make it a max heap
        # we start from scratch after adding all of the values to the heap
        # pick the one with the most occurences
        # then keep removing, if we've gone through all of the values
        # return ""

        counts = Counter(s)
        heap = [(-freq, ch) for ch, freq in counts.items()]
        heapq.heapify(heap)

        out = []
        prev_freq, prev_ch = 0, ""

        # while we still have items in the heap
        while heap:
            # get the most occuring one thats not the previous one
            freq, ch = heapq.heappop(heap)
            # insert it into out
            out.append(ch)

            # have to account for weird negative max heap stuff
            if prev_freq < 0: # if we still have items we need to use
                heapq.heappush(heap, (prev_freq, prev_ch))
            
            freq += 1

            prev_ch = ch
            prev_freq = freq

            # update which one we just previously used


        return ''.join(out) if len(out) == len(s) else ""