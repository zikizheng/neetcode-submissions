class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_mp = collections.defaultdict(set)
        col_mp = collections.defaultdict(set)
        sqr_mp = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in row_mp[row] or
                    board[row][col] in col_mp[col] or
                    board[row][col] in sqr_mp[(row // 3, col // 3)]):
                    return False
                row_mp[row].add(board[row][col])
                col_mp[col].add(board[row][col])
                sqr_mp[(row // 3, col // 3)].add(board[row][col])
        return True