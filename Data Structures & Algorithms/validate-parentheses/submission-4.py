class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        lookup = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []


        for c in s:
            if c not in lookup.keys():
                stack.append(c)
            elif stack and lookup[c] == stack[-1]:
                stack.pop()
        
            else:
                return False

        return not stack
