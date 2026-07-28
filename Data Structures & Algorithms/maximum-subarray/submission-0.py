class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = 0
        globalMax = nums[0]

        for num in nums:
            currMax = max(num + currMax, num)
            globalMax = max(currMax, globalMax)
        
        return globalMax if currMax > 0 else max(nums)