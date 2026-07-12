class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + "$" + haystack
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i < r:
                z[i] = min(r-i, z[i-l])
            while z[i] + i < n and s[z[i]] == s[z[i] + i]:
                z[i] += 1
            if z[i] + i > r:
                l, r = i, z[i] + i
        
        m = len(needle)
        for i in range(m + 1, n):
            if z[i] == m:
                return i - m - 1
        return -1