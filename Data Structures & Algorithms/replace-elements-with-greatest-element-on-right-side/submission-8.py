class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        temp = -1
        for i in range(len(arr)-1, -1, -1):
            res[i] = temp
            temp = max(temp, arr[i])
        return res