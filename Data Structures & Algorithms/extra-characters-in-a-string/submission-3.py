class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False

class Trie:
    def __init__(self, words):
        self.root = Node()

        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]

            curr.terminal = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root


        dp = {}

        def dfs(i):
            if i == len(s):
                return 0 
            
            # take or skip

            if i in dp:
                return dp[i]

            res = 1 + dfs(i+1)




            curr = trie

            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]

                if curr.terminal:
                    res = min(res, dfs(j+1))

            dp[i] = res
            return res

        
        return dfs(0)