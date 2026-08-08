class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen = set()
        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)
            res = 1
            for nei in adj[node]:
                res += dfs(nei)
            return res

        res = 0
        for node in range(n):
            if dfs(node) > 0:
                res += 1
        return res