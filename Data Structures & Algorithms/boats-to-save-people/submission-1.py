class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1
        j = 0
        for i in range(len(people)):
            while count[j] == 0:
                j += 1
            people[i] = j
            count[j] -= 1

        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1
            r -= 1
            res += 1
        return res