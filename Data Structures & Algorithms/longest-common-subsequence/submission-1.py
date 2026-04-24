class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            
            elif (i, j) not in memo:
                if text1[i] == text2[j]:
                    memo[(i, j)] = helper(i-1, j-1) + 1
                else:
                    memo[(i, j)] = max(helper(i, j-1), helper(i-1, j))
            
            return memo[(i,j)]



        return helper(len(text1)-1, len(text2)-1)
        