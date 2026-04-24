class Solution:
    def numDecodings(self, s: str) -> int:
        self.count = 0

        def is_valid(num):
            if len(num) == 1:
                num = int(num)
                return num > 0
            if len(num) == 2:
                return num[0] != '0' and 0 < int(num) <= 26
            return True

        def backtrack(i):
            if i == len(s):
                self.count += 1
            else:
                if i+ 1 <= len(s) and is_valid(s[i:i+1]):
                    backtrack(i+1)
                if i + 2 <= len(s) and is_valid(s[i:i+2]):
                    backtrack(i+2)
        backtrack(0)
        
        return self.count