class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen = set()

        def dfs(curr, par):
            if curr in seen:
                return False
            seen.add(curr)
            for nxt in adj[curr]:
                if nxt == par:
                    continue
                if nxt in seen:
                    return False
                if not dfs(nxt, curr):
                    return False
            return True
        
        return dfs(0, -1) and len(seen) == n