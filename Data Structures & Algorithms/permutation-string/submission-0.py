class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        l, r = 0, len(s1)

        for i in range(len(s2)-len(s1)+1):
            curr_count = Counter(s2[l:r])
            if curr_count == s1_count:
                return True
            l += 1
            r += 1
        return False
        