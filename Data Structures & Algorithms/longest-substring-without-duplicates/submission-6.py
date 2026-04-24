class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        lookup = defaultdict(int)

        l = 0
        for r, curr in enumerate(s):
            lookup[curr]+=1

            while lookup[curr] > 1:
                lookup[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)



        return longest
        