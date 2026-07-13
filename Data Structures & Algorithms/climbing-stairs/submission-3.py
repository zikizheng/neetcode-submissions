class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        onestep, twosteps = 1, 2
        for i in range(3, n+1):
            temp = twosteps
            twosteps = onestep + twosteps
            onestep = temp
        return twosteps