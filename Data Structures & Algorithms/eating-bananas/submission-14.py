class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = l + (r - l) // 2
            totalP = 0
            for p in piles:
                totalP += math.ceil(p / k)
            if totalP <= h:
                r = k
            else:
                l = k + 1
        return l