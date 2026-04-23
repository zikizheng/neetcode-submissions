class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s)-1
        res = 0
        while s[p] == ' ':
            p -= 1
        while p >= 0 and s[p] != ' ':
            p -= 1
            res += 1
        return res