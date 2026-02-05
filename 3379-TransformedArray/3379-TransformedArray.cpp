// Last updated: 2/5/2026, 10:34:37 AM
1class Solution {
2 public:
3  vector<int> constructTransformedArray(vector<int>& nums) {
4    const int n = nums.size();
5    vector<int> ans;
6
7    for (int i = 0; i < n; ++i)
8      ans.push_back(nums[(i + nums[i] % n + n) % n]);
9
10    return ans;
11  }
12};