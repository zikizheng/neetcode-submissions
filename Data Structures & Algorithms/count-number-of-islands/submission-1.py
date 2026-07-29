class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        stack = [(0, 0)]
        res = 0

        def dfs(r, c):
            for dr, dc in directions:
                R, C = r + dr, c + dc
                if 0 <= R < ROWS and 0 <= C < COLS and grid[R][C] == "1":
                    grid[R][C] = "0"
                    dfs(R, C)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res