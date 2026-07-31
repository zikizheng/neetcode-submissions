class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        pos = [0] * ROWS
        cur_max = i = 0
        while True:
            for j in range(ROWS):
                while pos[j] < COLS and mat[j][pos[j]] < cur_max:
                    pos[j] += 1
                if pos[j] == COLS:
                    return -1
                if mat[j][pos[j]] > cur_max:
                    i = 1
                    cur_max = mat[j][pos[j]]
                else:
                    i += 1
                    if i == ROWS:
                        return cur_max