class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        res = []
        for n in count:
            if count[n] > len(nums) / 3:
                res.append(n)
        return res