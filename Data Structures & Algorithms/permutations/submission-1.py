class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)

        def dfs(i, path):
            if len(path) == n:
                out.append(path[:])
                return

            for curr in nums:
                if curr in path:
                    continue
                dfs(i+1, path + [curr])


        dfs(0, [])
        return out

        