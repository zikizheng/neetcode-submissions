class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        p = 1
        for i in range(len(nums)):
            p *= nums[i]
            prefix[i] = p
        suffix = [1] * len(nums)
        s = 1
        for i in range(len(nums) - 1, -1, -1):
            s *= nums[i]
            suffix[i] = s
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i > 0:
                res[i] *= prefix[i-1]
            if i < len(nums) - 1:
                res[i] *= suffix[i+1]
        
        return res