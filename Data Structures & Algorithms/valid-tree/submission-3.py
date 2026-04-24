class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        visited.add(0)
        
        s = [0]

        while s:
            node = s.pop()
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    s.append(neighbor)
        return len(visited) == n

