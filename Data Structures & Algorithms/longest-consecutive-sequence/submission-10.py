class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        seq = {}
        for num in nums:
            if num-1 not in numSet:
                seq[num] = 0
                i = 0
                while num + i in numSet:
                    seq[num] += 1
                    i += 1
        return max(seq.values()) if seq else 0