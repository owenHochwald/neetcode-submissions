class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        out = []


        # what do we want to do?
            # when we add a dot, we want to make sure that 0 <= int(section) <= 256
                # we want to go at max 3 steps ahead, we want to validate before sending along
                # if something is not valid, cancel before sending along
                # if we have something like "255", we could do "2", "25", and "255"
                    # we could loop back from 3 or from 1, 2, 3
                # if we have something is valid, advance i by that amount and add to the path!


        def dfs(start: int , path: list):
            if len(path) == 4:
                if start == n:
                    out.append('.'.join(path))
                return
            # backtracking formula

            for length in [1,2,3]:
                end = start + length

                if end > n:
                    return

                section = s[start: end]
                if len(section) > 1 and section[0] =='0':
                    return

                if int(section) <= 255:
                    dfs(end, path + [section])

        dfs(0, [])

        return out 