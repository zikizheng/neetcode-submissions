class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            row = []
            for j in range(1, i+1):
                if j == 1 or j == i:
                    row.append(1)
                else:
                    row.append(res[i-2][j-1] + res[i-2][j-2])
            res.append(row)
        return res