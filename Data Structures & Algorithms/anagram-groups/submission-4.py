class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            lookup = [0] * 26
            for i in s:
                lookup[ord(i) - ord('a')]+=1
            anagrams[tuple(lookup)].append(s)
        return list(anagrams.values())
