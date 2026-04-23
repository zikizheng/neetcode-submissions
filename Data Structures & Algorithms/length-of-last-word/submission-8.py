class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        temp = len(s) - 1
        while temp >= 0 and s[temp] == ' ':
            temp -= 1
        while temp >= 0 and s[temp] != ' ':
            res += 1
            temp -= 1
        return res