class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS from any node should lead us to being able to visit every single edge
            # # of edges visited should equal total number of edge
        # should not have seen stuff
        
        if not edges:
            if n == 1:
                return True
            return False
        
        lookup = defaultdict(list) 
        for u, v in edges:
            lookup[v].append(u)
            lookup[u].append(v)

        q = deque([0])
        seen = set()

        while q:
            node = q.popleft()
            print("saw node: ", node)

            if node in seen:
                return False
            
            seen.add(node)

            for neigh in lookup[node]:
                if neigh not in seen:
                    q.append(neigh)
        
        print(len(seen))
        return len(seen) == n