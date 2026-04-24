class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in ['(', '[', '{']:
                stack.append(p)
            elif p == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif p == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif p == ']':
                if not stack or stack.pop() != '[':
                    return False
            
        return not stack

        