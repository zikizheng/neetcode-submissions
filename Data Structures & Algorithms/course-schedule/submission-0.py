class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i: [] for i in range(numCourses)}
        visited = set()

        for a, b in prerequisites:
            mp[a].append(b)

        def dfs(course):
            if course in visited:
                return False
            if mp[course] == []:
                return True

            visited.add(course)
            for prereq in mp[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            mp[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True