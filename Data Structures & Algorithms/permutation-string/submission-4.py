class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm_counter = Counter(s1)
        window = len(s1)

        for i in range(0, len(s2) - window + 1):
            window_counter = Counter(s2[i:i+window])
            if window_counter == perm_counter:
                return True
            
        return False