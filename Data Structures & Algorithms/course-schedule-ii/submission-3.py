class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for a, b in prerequisites:
            mp[a].append(b)
        
        seen, cycle = set(), set()

        res = []

        def dfs(c):
            if c in seen:
                return True
            if c in cycle:
                return False
            cycle.add(c)

            for p in mp[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            seen.add(c)
            res.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res