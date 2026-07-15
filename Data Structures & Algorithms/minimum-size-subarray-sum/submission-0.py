class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixSum = [0] * len(nums)
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefixSum[i] = prefix
        
        res = float("infinity")
        l = 0
        for r in range(len(nums)):
            if prefixSum[r] >= target:
                while prefixSum[r] - prefixSum[l] >= target:
                    l += 1
                res = min(res, r - l + 1)
        return 0 if res == float("infinity") else res