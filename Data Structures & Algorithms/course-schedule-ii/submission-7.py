class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        cnts = [0] * numCourses

        for crs, prereq in prerequisites:
            adj[prereq].append(crs)
            cnts[crs] += 1
        
        q = collections.deque()

        for i in range(len(cnts)):
            if cnts[i] == 0:
                q.append(i)
        
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)
            for nxt in adj[crs]:
                cnts[nxt] -= 1
                if cnts[nxt] == 0:
                    q.append(nxt)
        
        return res if len(res) == numCourses else []