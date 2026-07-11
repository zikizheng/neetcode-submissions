class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in cols[c]
                    or board[r][c] in rows[r]
                    or board[r][c] in squares[c//3, r//3]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[c//3, r//3].add(board[r][c])
        return True