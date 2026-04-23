class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, l, = 0, 0
        seen = {}
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            if (r-l+1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            else:
                res = max(r-l+1, res)
        return res