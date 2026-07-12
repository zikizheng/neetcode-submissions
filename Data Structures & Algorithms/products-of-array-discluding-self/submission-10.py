class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref = 1
        for i in range(len(nums)):
            res.append(pref)
            pref *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res