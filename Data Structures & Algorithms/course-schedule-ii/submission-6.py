class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        cnts = [0] * numCourses

        for crs, prereq in prerequisites:
            mp[prereq].append(crs)
            cnts[crs] += 1
        
        q = collections.deque()

        for i in range(len(cnts)):
            if cnts[i] == 0:
                q.append(i)
        
        res = []

        while q:
            crs = q.popleft()
            res.append(crs)
            for post in mp[crs]:
                cnts[post] -= 1
                if cnts[post] == 0:
                    q.append(post)
                    
        
        return res if len(res) == numCourses else []