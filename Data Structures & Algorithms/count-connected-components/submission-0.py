class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        

        def bfs(node):
            q = deque([node])
            seen.add(node)
            while q:
                curr = q.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append(neighbor)

            

        res = 0
        for node in range(n):
            if node not in seen:
                bfs(node)
                res += 1
        return res

        