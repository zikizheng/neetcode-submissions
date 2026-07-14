class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]

        res = 0

        while l < r:
            if height[l] < height[r]:
                res += maxl - height[l]
                l += 1
                maxl = max(height[l], maxl)
            else:
                res += maxr - height[r]
                r -= 1
                maxr = max(height[r], maxr)
        return res