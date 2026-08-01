class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        two, one = 1, 2
        for i in range(2, n):
            two, one = one, two + one
        return one