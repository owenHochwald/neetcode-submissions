from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        out = []
        for k,v in anagrams.items():
            out.append(v)
        
        return out
        