class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for crs, prereq in prerequisites:
            adj[crs].append(prereq)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if adj[crs] == []:
                return True
            visited.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True