class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = res = 0
        for num in nums:
            if curr == 0:
                res = num
            curr += 1 if res == num else -1
        return res