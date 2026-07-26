class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = { 0: 1}
        res = s = 0
        for num in nums:
            s += num
            diff = s - k
            res += mp.get(diff, 0)
            mp[s] = mp.get(s, 0) + 1
        return res