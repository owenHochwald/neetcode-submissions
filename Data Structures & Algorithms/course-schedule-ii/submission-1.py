class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_list = defaultdict(list)
        for course, prereq in prerequisites:
            in_list[prereq].append(course)

        ins = [0] * numCourses

        for course, _ in prerequisites:
            ins[course] += 1
        
        out = []

        q = deque([x for x in range(numCourses) if ins[x] == 0])
        print(ins)
        print(q)

        while q:
            node = q.pop()
            out.append(node)
            # relax neighbors
            for neigh in in_list[node]:
                ins[neigh] -= 1
                if ins[neigh] == 0:
                    q.append(neigh)
                    
        if len(out) != numCourses:
            return []
        return out
        