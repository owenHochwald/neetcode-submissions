class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(word: str) -> bool:
            l, r = 0, len(word) -1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                start_keep = s[:end] + s[end+1:]
                end_keep = s[:start] + s[start+1:]
                return check_palindrome(start_keep) or check_palindrome(end_keep)
            start += 1
            end -= 1

        return check_palindrome(s) 
