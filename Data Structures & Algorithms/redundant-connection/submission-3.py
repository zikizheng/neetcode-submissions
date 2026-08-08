class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        cnts = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            cnts[u] += 1
            cnts[v] += 1
        
        q = collections.deque()

        for i in range(1, n + 1):
            if cnts[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            cnts[node] -= 1
            for nei in adj[node]:
                cnts[nei] -= 1
                if cnts[nei] == 1:
                    q.append(nei)
        print(cnts)
        
        for u, v in reversed(edges):
            if cnts[u] == cnts[v] == 2:
                return [u, v]
        return []