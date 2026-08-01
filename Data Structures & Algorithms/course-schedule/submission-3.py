class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for a, b in prerequisites:
            mp[a].append(b)
        
        seen = set()
        def dfs(crs):
            if crs in seen:
                return False
            seen.add(crs)
            for n in mp[crs]:
                if not dfs(n):
                    return False
            mp[crs] = []
            seen.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True