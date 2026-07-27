class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex - 1)
        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            res[i] = prev[i] + prev[i - 1]
        return res