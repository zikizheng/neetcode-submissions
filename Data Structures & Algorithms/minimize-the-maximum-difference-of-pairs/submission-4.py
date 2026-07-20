class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        res = float('inf')
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        res = r
        
        def verify(threshold):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i + 1] - nums[i]) <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False
                

        while l <= r:
            m = l + (r - l) // 2
            if verify(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res