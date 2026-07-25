class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixMatrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for row in range(1, len(self.prefixMatrix)):
            s = 0
            for col in range(1, len(self.prefixMatrix[0])):
                s += matrix[row - 1][col - 1]
                a = self.prefixMatrix[row-1][col]
                self.prefixMatrix[row][col] = s + a

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        br = self.prefixMatrix[row2+1][col2+1]
        tr = self.prefixMatrix[row1][col2+1]
        bl = self.prefixMatrix[row2+1][col1]
        tl = self.prefixMatrix[row1][col1]

        return br - tr - bl + tl       


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)