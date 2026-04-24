class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, len(s1)
        counter = Counter(s2[l:r])
        targetCounter = Counter(s1)

        while r < len(s2):
            if counter == targetCounter:
                return True
            
            counter[s2[r]]+=1
            r += 1
            counter[s2[l]]-=1
            l += 1
        return counter == targetCounter
