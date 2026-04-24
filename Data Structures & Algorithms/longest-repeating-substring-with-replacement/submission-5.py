class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = Counter()
        l = 0
        max_freq = 0
        longest = 0

        for i in range(len(s)):
            freqs[s[i]] += 1
            max_freq = max(max_freq, freqs[s[i]])

            while (i - l + 1) > k + max_freq:
                freqs[s[l]] -= 1
                l += 1
            longest = max(longest, i - l + 1)
        return longest
