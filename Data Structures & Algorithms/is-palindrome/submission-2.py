import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r"[a-z|A-Z|0-9]", s)).lower()
        for i in range(0, len(s)//2):
            if s[i] != s[(-1-i)]:
                return False
        return True