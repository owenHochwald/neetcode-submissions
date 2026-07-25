class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # looks like we want to add the weights ourselves
        # a node could be connected to any of the other nodes
        # maybe we need to embed each node with (n-1) other connections based on weight?
        # then run kruskals and find the sum?


        # embed / calculate all of the edges weights
            # for this part, we don't even care about the nodes! the nodes are just there to help us find the edge weight
            # map an edge weight: node

        # sort all of the edges

        # while we haven't picked v-1 edges
            # pick the smallest edge that is "new" or doesn't form a cycle 
        
        # gonna go with prims algorithm for this part

        graph = defaultdict(list)

        for i, p in enumerate(points):
            for j, g in enumerate(points):
                if i == j:
                    continue
                dist = abs(p[0] - g[0]) + abs(p[1] - g[1]) 
                graph[i].append([dist, j])


        def prims(n, graph):

            seen = set()
            h = [(0, 0)]
            total = 0

            while h and len(seen) < n:
                w, node = heapq.heappop(h)

                if node in seen:
                    continue

                seen.add(node)
                total += w

                for neigh in graph[node]:
                    if neigh[1] not in seen:
                        heapq.heappush(h, neigh)
                        




            return total

        return prims(len(points), graph)