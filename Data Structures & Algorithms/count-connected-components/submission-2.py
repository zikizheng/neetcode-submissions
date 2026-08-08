class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen = set()
        def dfs(node):
            if node in seen:
                return False
            seen.add(node)
            for nei in adj[node]:
                dfs(nei)
            return True

        res = 0
        for node in range(n):
            if dfs(node):
                res += 1
        return res