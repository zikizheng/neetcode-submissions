class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        while l < len(s):
            if r == len(t):
                return False
            if s[l] == t[r]:
                l += 1
            r += 1
        return True