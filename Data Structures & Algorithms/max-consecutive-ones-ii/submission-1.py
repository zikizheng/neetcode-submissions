class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        numZeroes = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                numZeroes += 1
            while numZeroes == 2:
                if nums[l] == 0:
                    numZeroes -= 1
                l += 1
            res = max(res, r - l + 1)
        return res