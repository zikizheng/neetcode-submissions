class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        cnts = [0] * numCourses
        
        for crs, prereq in prerequisites:
            adj[prereq].append(crs)
            cnts[crs] += 1
        
        q = collections.deque()

        for crs in range(len(cnts)):
            if cnts[crs] == 0:
                q.append(crs)
        
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)
            for postreq in adj[crs]:
                cnts[postreq] -= 1
                if cnts[postreq] == 0:
                    q.append(postreq)
        
        return res if len(res) == numCourses else []