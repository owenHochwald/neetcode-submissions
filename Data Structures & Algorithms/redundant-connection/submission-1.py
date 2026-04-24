class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 == r2:
                return False
            parent[r1] = r2
            return True
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        for i, j in edges:
            if not union(i, j):
                return [i, j]

        