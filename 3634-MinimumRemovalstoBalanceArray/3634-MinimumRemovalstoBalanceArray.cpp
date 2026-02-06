// Last updated: 2/6/2026, 8:20:39 AM
1class Solution {
2public:
3    int minRemoval(vector<int>& nums, int k) {
4        ranges::sort(nums);
5        int cnt = 0;
6        int n = nums.size();
7        for (int i = 0; i < n; ++i) {
8            int j = n;
9            if (1LL * nums[i] * k <= nums[n - 1]) {
10                j = upper_bound(nums.begin(), nums.end(), 1LL * nums[i] * k) - nums.begin();
11            }
12            cnt = max(cnt, j - i);
13        }
14        return n - cnt;
15    }
16};