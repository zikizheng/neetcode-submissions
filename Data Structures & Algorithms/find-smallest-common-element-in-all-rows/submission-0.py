class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        for num in mat[0]:
            res = []
            for ls in mat:
                l, r = 0, len(ls) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if ls[m] == num:
                        res.append(ls[m])
                        break
                    elif ls[m] < num:
                        l = m + 1
                    elif ls[m] > num:
                        r = m - 1
            if len(res) == len(mat):
                return res[0]
        return -1
                