class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 1
        l, r = 0, 0
        
        window = set()
        while r < len(s):
            if window and s[r] not in window:
                longest = max(longest, r - l + 1)
                window.add(s[r])
                r += 1
            else:
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
                r += 1
        return longest 


        