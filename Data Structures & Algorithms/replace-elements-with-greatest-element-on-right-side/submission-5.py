class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        res = [-1] * len(arr)
        m = -1
        for i in range(len(arr)-1, -1, -1):
            res[i] = m
            m = max(m, arr[i])
        return res