class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one, two = 1, 2
        for _ in range(2, n):
            temp = two
            two = one + two
            one = temp
        return two