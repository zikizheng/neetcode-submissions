class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        l, r = 0, 0
        res = 0
        while r < len(target):
            temp = r
            while l < len(source):
                if r == len(target):
                    return res + 1
                if source[l] == target[r]:
                    r += 1
                l += 1
            l = 0
            res += 1
            if r == temp:
                return -1
        return res