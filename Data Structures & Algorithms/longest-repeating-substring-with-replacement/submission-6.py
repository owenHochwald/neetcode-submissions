from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = Counter()
        l = 0
        max_freq = 0
        longest = 0

        for r in range(len(s)):
            freqs[s[r]]+=1
            max_freq = max(max_freq, freqs[s[r]])

            while (r-l+1) > k + max_freq:
                freqs[s[l]]-=1
                l += 1
            longest = max(longest, r-l+1)
        return longest