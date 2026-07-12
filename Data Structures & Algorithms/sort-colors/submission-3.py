class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        i = 0
        for c in range(3):
            while count[c]:
                nums[i] = c
                count[c] -= 1
                i += 1