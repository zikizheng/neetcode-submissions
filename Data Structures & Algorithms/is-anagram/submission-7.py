class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = [0]*26
        for i in range(len(s)):
            seen[ord(s[i].lower()) - ord('a')] += 1
            seen[ord(t[i].lower()) - ord('a')] -= 1
        for i in seen:
            if i != 0:
                return False
        return True