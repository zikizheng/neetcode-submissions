class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            mp[a].append(b)
        
        visiting = set()
        def dfs(c):
            if mp[c] == []:
                return True
            if c in visiting:
                return False
            visiting.add(c)
            for prereq in mp[c]:
                if not dfs(prereq):
                    return False
            visiting.remove(c)
            mp[c] = []
            return True
            
        for c in range(numCourses):
            if not dfs(c): 
                return False
        return True