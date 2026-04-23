class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        temp = 0
        for n in nums:
            temp += n
            self.prefix.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix[right] - self.prefix[left-1]
        return self.prefix[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)