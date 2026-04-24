class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, neighbor, cost in times:
            adj[source].append([neighbor, cost])
        distances = {node: 1e7 for node in range(1, n+1)}
        distances[k] = 0
        pq = [(0, k)]


        while pq:
            curr_d, curr_node = heapq.heappop(pq)

            if curr_d > distances[curr_node]:
                continue
            
            for neighbor, weight in adj[curr_node]:
                distance = weight + curr_d

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, [distance, neighbor])
        
        distance = max(distances.values())
        return -1 if distance == 1e7 else distance

        