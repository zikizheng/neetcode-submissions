class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = globalMin = nums[0]
        currMax = currMin = 0
        total = sum(nums)
        for num in nums:
            currMax = max(num, currMax + num)
            globalMax = max(currMax, globalMax)

            currMin = min(num, currMin + num)
            globalMin = min(currMin, globalMin)
        
        return max(globalMax, total - globalMin) if currMax > 0 else max(nums)