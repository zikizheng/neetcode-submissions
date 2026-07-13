class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prevRow = [1]
        for i in range(rowIndex+1):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = prevRow[j] + prevRow[j-1]
            prevRow = row
        return row