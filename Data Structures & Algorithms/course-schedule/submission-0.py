class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adaj = defaultdict(list)
        for course, prereq in prerequisites:
            adaj[prereq].append(course)
        
        indegs = [0] * numCourses

        for u, v in prerequisites:
            indegs[u] += 1
        
        q = deque([x for x in range(len(indegs)) if indegs[x] == 0])

        count = 0

        while q:
            node = q.popleft()
            count += 1
            for neighbor in adaj[node]:
                indegs[neighbor] -= 1
                if indegs[neighbor]== 0:
                    q.append(neighbor)
        
        return count == numCourses
