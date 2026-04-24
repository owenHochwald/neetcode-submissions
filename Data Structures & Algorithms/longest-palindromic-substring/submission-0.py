class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        longest = ""
        for i in range(len(s)):
            # odd
            p1 = expand(i, i)
            if len(p1) > len(longest):
                longest = p1

            p2 = expand(i, i+1)
            if len(p2) > len(longest):
                longest = p2


            # even



        return longest
        