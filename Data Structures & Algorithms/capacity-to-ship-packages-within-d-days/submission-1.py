class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        def canShip(day):
            total = 1
            currDay = 0
            for w in weights:
                if currDay + w > day:
                    total += 1
                    currDay = w
                else:
                    currDay += w
            return total
        
        while l < r:
            m = l + (r - l) // 2
            if canShip(m) > days:
                l = m + 1
            else:
                r = m
        return l
