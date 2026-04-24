class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            return word == word[::-1]

        out = []

        def backtrack(start, path):
            if start >= len(s):
                out.append(path[:])
                return
            else:
                for end in range(start + 1, len(s) + 1):
                    if isPalindrome(s[start:end]):
                        path.append(s[start:end])
                        backtrack(end, path)
                        path.pop()

        backtrack(0, [])
        return out
        