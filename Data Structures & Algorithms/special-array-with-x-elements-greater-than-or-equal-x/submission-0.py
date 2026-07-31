class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        def special(m):
            cnt = 0
            for num in nums:
                if num >= m:
                    cnt += 1
            return cnt

        while l <= r:
            m = l + (r - l) // 2
            if special(m) == m:
                return m
            if special(m) > m:
                l = m + 1
            else:
                r = m - 1
        return -1
        
        