class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = globalMin = nums[0]
        currMax = 0
        currMin = 0
        total = 0

        for num in nums:
            currMax = max(num + currMax, num)
            globalMax = max(globalMax, currMax)

            currMin = min(num + currMin, num)
            globalMin = min(globalMin, currMin)

            total += num
        
        return max(globalMax, total - globalMin) if globalMax > 0 else max(nums)