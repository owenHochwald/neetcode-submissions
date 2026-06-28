class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1 

        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)



        return self.count 