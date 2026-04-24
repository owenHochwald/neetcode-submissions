class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        longest = 0
        counter = Counter()

        for r in range(len(s)):
            counter[s[r]]+=1
            max_freq = max(max_freq, counter[s[r]])

            while (r-l+1) > max_freq + k:
                counter[s[l]]-=1
                l += 1
            longest = r - l + 1
        return longest


        