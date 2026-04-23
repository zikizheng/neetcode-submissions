class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        p = len(s) - 1
        while s[p] == ' ':
            p -= 1
        while p >= 0 and s[p] != ' ':
            res += 1
            p -= 1
        return res 