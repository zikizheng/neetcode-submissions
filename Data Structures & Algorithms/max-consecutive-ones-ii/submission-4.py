class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        zeros = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
                if zeros == 2:
                    while nums[l] != 0:
                        l += 1
                    l += 1
                    zeros -= 1
            res = max(r - l + 1, res)
        return res