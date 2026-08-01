class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        two, one = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            two, one = one, max(one, nums[i] + two)
        return one