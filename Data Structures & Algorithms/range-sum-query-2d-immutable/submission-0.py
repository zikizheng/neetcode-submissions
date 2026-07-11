class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefMat = [[0] * (cols+1) for c in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                self.prefMat[r+1][c+1] = prefix + self.prefMat[r][c+1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefMat[row2+1][col2+1]
        above = self.prefMat[row1][col2+1]
        left = self.prefMat[row2+1][col1]
        topleft = self.prefMat[row1][col1]

        return bottomRight - above - left + topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)