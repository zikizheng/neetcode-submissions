class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for crs, prereq in prerequisites:
            mp[crs].append(prereq)
        
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            if mp[crs] == []:
                return True
            
            seen.add(crs)
            for prereq in mp[crs]:
                if not dfs(prereq):
                    return False
            seen.remove(crs)
            mp[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True