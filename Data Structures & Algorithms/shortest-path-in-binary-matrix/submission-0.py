class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        if grid[0][0] or grid[N-1][N-1]:
            return -1

        directions = [[1, 1], [1, -1], [-1, 1], [-1, -1], [0, 1], [0, -1], [1, 0], [-1, 0]]
        q = collections.deque([(0, 0, 1)])

        while q:
            r, c, l = q.popleft()
            if r == N - 1 and c == N - 1:
                return l
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, l + 1))
        return -1