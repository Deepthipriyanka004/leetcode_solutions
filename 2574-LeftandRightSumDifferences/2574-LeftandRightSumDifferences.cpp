// Last updated: 6/6/2026, 11:38:13 AM
1class Solution {
2public:
3    vector<int> leftRightDifference(vector<int>& nums) {
4        int n = nums.size();
5
6        vector<int> ans(n);
7        vector<int> leftSum(n);
8        vector<int> rightSum(n);
9
10        int prefix = 0;
11        int suffix = 0;
12
13        for (int i = 0; i < n; i++) {
14            if (i > 0)
15                prefix += nums[i - 1];
16            leftSum[i] = prefix;
17        }
18
19        for (int i = n - 1; i >= 0; i--) {
20            if (i + 1 < n)
21                suffix += nums[i + 1];
22            rightSum[i] = suffix;
23        }
24
25        for (int i = 0; i < n; i++) {
26            ans[i] = abs(leftSum[i] - rightSum[i]);
27        }
28
29        return ans;
30    }
31};