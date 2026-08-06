class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = defaultdict(list)
        if len(edges) != n - 1:
            return False

        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
        
        seen = set()

        def dfs(curr, parent):
            if curr in seen:
                return False
            
            seen.add(curr)
            for nxt in mp[curr]:
                if nxt == parent:
                    continue
                if not dfs(nxt, curr):
                    return False
            return True
        
        return dfs(0, -1) and len(seen) == n