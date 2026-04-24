class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(filter(str.isalnum, s)).lower()

        l, r = 0, len(clean) -1
        print(clean)
        while l < r:
            print(clean[l], clean[r])
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1
        return True