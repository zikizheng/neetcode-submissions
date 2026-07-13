class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prevRow = [1]
        row = [1] * (rowIndex + 1)
        for i in range(rowIndex+1):
            for j in range(i - 1, 0, -1):
                row[j] = prevRow[j] + prevRow[j-1]
            prevRow = row
        return row