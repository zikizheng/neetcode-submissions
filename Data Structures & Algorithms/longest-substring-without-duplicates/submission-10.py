class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                res = max(r-l+1, res)
                seen.add(s[r])
        return res

