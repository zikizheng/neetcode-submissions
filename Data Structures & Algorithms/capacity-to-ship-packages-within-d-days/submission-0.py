class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = l + (r - l) // 2
            currDay = 0
            totalDays = 1
            for w in weights:
                if w + currDay > m:
                    totalDays += 1
                    currDay = w
                else:
                    currDay += w

            if totalDays > days:
                l = m + 1
            elif totalDays <= days:
                r = m
        return l
