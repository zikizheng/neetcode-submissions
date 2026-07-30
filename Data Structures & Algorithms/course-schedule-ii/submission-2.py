class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {i: [] for i in range(numCourses)}
        res = []
        visit, cycle = set(), set()
        
        for a, b in prerequisites:
            mp[a].append(b)
        
        def dfs(c):
            if c in cycle:
                return False
            if c in visit: 
                return True
            cycle.add(c)
            for n in mp[c]:
                if not dfs(n):
                    return False
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res