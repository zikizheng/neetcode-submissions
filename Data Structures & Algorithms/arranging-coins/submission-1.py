class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while n - i > 0:
            i += 1
            n -= i
        return i