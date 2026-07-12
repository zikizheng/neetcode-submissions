class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        k = len(nums)
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                k -= 1
                r -= 1
            else:
                l += 1
        return k