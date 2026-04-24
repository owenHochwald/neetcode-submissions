class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # [1,2,3]

        # no duplicates!
        # [], [1], [1,2], [1,2,3], [2], [2,3]

        # at each step, we add unique solutions!

        # recursive backtracking solutions

            # when len path == nums?
                # add to set, return and finish!

            # from our current index -> recurse on all after this!

            # from our range we append a number -> recurse after this position -> pop and restart
            # do this for everything?


        out = []

        def backtrack(start, path):
            if len(path) <= len(nums):
                # add to the solution:
                out.append(path[:])

                # for everything after in this range!
                for i in range(start, len(nums)):
                    # add to the path (we want ALLLLL lengths solutions)
                    path.append(nums[i])
                    # recurse
                    backtrack( i+1, path)
                    # undo
                    path.pop()
                


        backtrack(0, [])
        return out


            