class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        # this needs to be n+1 so that we can have the first index be true and give us something to "jump off of"
        # we can always segment something that has no chars

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # optimization

        return dp[n]

        
        