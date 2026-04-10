// Last updated: 4/10/2026, 12:18:14 PM
1class Solution {
2public:
3    int minimumDistance(vector<int>& nums) {
4        int n = nums.size();
5        unordered_map<int, vector<int>> g;
6        for (int i = 0; i < n; ++i) {
7            g[nums[i]].push_back(i);
8        }
9        const int inf = 1 << 30;
10        int ans = inf;
11        for (auto& [_, ls] : g) {
12            int m = ls.size();
13            for (int h = 0; h < m - 2; ++h) {
14                int i = ls[h];
15                int k = ls[h + 2];
16                int t = (k - i) * 2;
17                ans = min(ans, t);
18            }
19        }
20        return ans == inf ? -1 : ans;
21    }
22};