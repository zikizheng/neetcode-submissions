class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def zfunction(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    k = i - l
                    z[i] = min(r-i+1, z[k])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z
        s = needle + "$" + haystack
        z = zfunction(s)
        for i in range(len(z)):
            if z[i] == len(needle):
                return i - len(needle) - 1
        return -1