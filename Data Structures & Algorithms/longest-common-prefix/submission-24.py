class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        
        res = ""
        for j in range(len(strs[0])):
            for i in range(1, n):
                if len(strs[i]) <= j or strs[i][j] != strs[0][j]:
                    return res
            res += strs[0][j]
        return res