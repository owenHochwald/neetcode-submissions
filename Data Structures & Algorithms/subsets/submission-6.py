class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)

        def dfs(i, path):
            if len(path) <= n:

                out.append(path[:])

                for j in range(i, n):
                    path.append(nums[j])
                    dfs(j + 1, path)
                    path.pop()



        dfs(0, [])

        return out
        