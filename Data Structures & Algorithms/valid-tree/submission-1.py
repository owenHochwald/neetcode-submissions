class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        visited = set()

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([0])
        visited.add(0)

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                q.append(neighbor)

        return len(visited) == n
