// Last updated: 5/1/2026, 10:09:22 AM
1class Solution {
2  public int maxRotateFunction(int[] nums) {
3    final int sum = Arrays.stream(nums).sum();
4    int f = 0;
5
6    // Calculate F(0) first.
7    for (int i = 0; i < nums.length; ++i)
8      f += i * nums[i];
9
10    int ans = f;
11
12    for (int i = nums.length - 1; i >= 0; --i) {
13      f += sum - nums.length * nums[i];
14      ans = Math.max(ans, f);
15    }
16
17    return ans;
18  }
19}