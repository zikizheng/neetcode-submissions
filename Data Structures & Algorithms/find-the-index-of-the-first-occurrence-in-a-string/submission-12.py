class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + "$" + haystack
        n = len(s)
        l, r = 0, 0
        z = [0] * n
        
        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while z[i] + i < n and s[z[i]] == s[z[i] + i]:
                z[i] += 1
            if z[i] + i < r:
                l, r = i, z[i] + i
        
        for i in range(len(needle) + 1, n):
            if z[i] == len(needle):
                return i - len(needle) - 1
        return -1