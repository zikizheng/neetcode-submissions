class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        zero = False
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                if zero:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                else:
                    zero = True
            res = max(r - l + 1, res)
        return res