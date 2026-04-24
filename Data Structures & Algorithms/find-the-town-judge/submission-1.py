class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # find the judge based on the trust
        # the just will trust no one
        # everyone else trusts the town judge
        # there is only one of these people

        # we just need to make a set of all the ais
            # at the end check if everyone is included in it
        # if so return -1

        seen = set()
        lookup = defaultdict(int)
        # the judge trusts no one
        for a, b in trust:
            seen.add(a)
            lookup[b] += 1

        # verify that everyone trusts the judge
        
        for i in range(1, n+1):
            if i not in seen and lookup[i] == n-1:
                return i
        return -1
