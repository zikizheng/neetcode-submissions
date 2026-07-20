class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1
        while l <= r:
            m = l + (r - l) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                break
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        row = m
        l, r = 0, COLS - 1

        while l <= r:
            m = l + (r - l) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False