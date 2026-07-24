class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 0, x
        res = 0
        while l < r:
            m = l + (r - l) // 2
            if m * m <= x:
                res = m
                l = m + 1
            else:
                r = m
        return res