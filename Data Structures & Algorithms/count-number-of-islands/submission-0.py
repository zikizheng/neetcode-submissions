class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        stack = [(0, 0)]
        res = 0
        seen = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    stack = [(r, c)]
                    while stack:
                        nr, nc = stack.pop()
                        for dr, dc in directions:
                            R, C = nr + dr, nc + dc
                            if 0 <= R < ROWS and 0 <= C < COLS and grid[R][C] == "1":
                                grid[R][C] = "0"
                                stack.append((R, C))
                    res += 1
        return res