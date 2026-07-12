class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums)-1)
    
    def mergeSort(self, nums: List[int], s: int, e: int) -> List[int]:
        if e - s + 1 <= 1:
            return nums
        m = s + (e - s) // 2
        self.mergeSort(nums, s, m)
        self.mergeSort(nums, m+1, e)

        l = nums[s: m+1]
        r = nums[m+1: e+1]

        i = 0
        j = 0
        k = s

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                nums[k] = l[i]
                i += 1
            else:
                nums[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            nums[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            nums[k] = r[j]
            j += 1
            k += 1
        
        return nums