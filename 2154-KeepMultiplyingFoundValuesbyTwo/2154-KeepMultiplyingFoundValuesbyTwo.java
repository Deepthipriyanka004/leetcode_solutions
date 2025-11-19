// Last updated: 11/19/2025, 8:58:21 AM
public class Solution {
    public int findFinalValue(int[] nums, int original) {
        int i = 0;
        while (i < nums.length) {
            if (nums[i] == original) {
                original = original * 2;
                i = -1;
            }
            i++;
        }
        return original;
    }
}