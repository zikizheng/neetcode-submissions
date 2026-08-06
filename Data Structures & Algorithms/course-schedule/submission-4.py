class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        cnts = [0] * numCourses
        courses = []
        for a, b in prerequisites:
            adj[b].append(a)
            cnts[a] += 1
        
        q = collections.deque()

        for i in range(len(cnts)):
            if cnts[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            courses.append(course)
            for prereq in adj[course]:
                cnts[prereq] -= 1
                if cnts[prereq] == 0:
                    q.append(prereq)

        return len(courses) == numCourses