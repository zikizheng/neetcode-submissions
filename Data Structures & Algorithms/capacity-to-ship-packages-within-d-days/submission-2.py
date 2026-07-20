class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            totalDays = 0
            currTotal = 0
            for w in weights:
                if currTotal + w > m:
                    totalDays += 1
                    currTotal = w
                else:
                    currTotal += w
            totalDays += 1 if currTotal else 0
            if totalDays <= days:
                r = m
            else:
                l = m + 1
        return l