class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        res = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            res[i] = rightMax
            rightMax = max(rightMax, arr[i])
        return res