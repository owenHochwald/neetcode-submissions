class Solution:
    def decodeString(self, s: str) -> str:
        # when we come across a "]", we pop from the stack and multiply by the number k
            # we prepend the stuff from the stack and s[1:] + int(s[0]) * curr
        # when we come across a "[", we start a new curr queue for our stack

        # invariant / convention: first element in the stack is the number of times to repeat

        # append to the output when not wrapped in the numbers 
        out = []

        stack = []
        curr_num = 0

        for c in s:
            if c.isdigit():
                curr_num = 10 *curr_num + int(c)
            elif c == '[':
                stack.append([curr_num, ''.join(out)])
                curr_num = 0
                out = []
            
            elif c == ']':
                times, prev = stack.pop()
                inner = ''.join(out)
                out = [prev]
                out.append(times * inner)

            else:
                out.append(c)
        




        return ''.join(out)