class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        p = set()
        a = set()
        q = collections.deque()
        def bfs(s):
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS 
                            and heights[r][c] <= heights[nr][nc] 
                            and (nr,nc) not in s):
                            s.add((nr, nc))
                            q.append([nr, nc])

        for col in range(COLS):
            q.append([0, col])
            p.add((0, col))
        for row in range(ROWS):
            q.append([row, 0])
            p.add((row, 0))

        bfs(p)
        
        for col in range(COLS):
            q.append([ROWS - 1, col])
            a.add((ROWS - 1, col))
        for row in range(ROWS):
            q.append([row, COLS - 1])
            a.add((row, COLS - 1))

        bfs(a)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in p and (r, c) in a:
                    res.append([r, c])
        return res