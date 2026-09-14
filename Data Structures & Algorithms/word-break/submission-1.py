from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        self.res = False

        @cache 
        def dfs(i, substring):
            if self.res:
                return
            if i == n:
                if not substring:
                    self.res = True
                return
            
            substring += s[i]
            if substring in word_set:
                dfs(i+1, "")
            
            dfs(i+1, substring)

        dfs(0, "")
        return self.res

