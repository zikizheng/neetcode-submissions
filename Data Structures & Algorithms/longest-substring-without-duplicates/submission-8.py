class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        while l < len(s):
            seen = set()
            curLen = 0
            r = l
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
                curLen += 1
                res = max(res, curLen)
            l += 1
        return res