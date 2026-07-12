class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + "$" + haystack
        l, r = 0, 0
        z = [0] * len(s)
        for i in range(1, len(s)):
            if i < r:
                z[i] = min(r-i, z[i-l])
            while i + z[i] < len(s) and s[z[i]] == s[z[i] + i]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i+z[i]
        for i in range(len(needle)+1, len(s)):
            if z[i] == len(needle):
                return i - len(needle) - 1
        return -1