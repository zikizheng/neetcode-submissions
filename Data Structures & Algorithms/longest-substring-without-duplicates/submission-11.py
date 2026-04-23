class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in sSet:
                sSet.remove(s[l])
                l += 1
            else:
                sSet.add(s[r])
                r += 1
                res = max(res, r-l)
        return res