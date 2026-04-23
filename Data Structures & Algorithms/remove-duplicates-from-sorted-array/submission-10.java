class Solution {
    public int removeDuplicates(int[] nums) {
        int length = nums.length;
        if (length < 2){
            return length;
        }
        int l = 1;
        for (int r = 1; r < length; r++){
            if (nums[r] != nums[r-1]){
                nums[l] = nums[r];
                l++;
            }
        }
        return l;
    }
}