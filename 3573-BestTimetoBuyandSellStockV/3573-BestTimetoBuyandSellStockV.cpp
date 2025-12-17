// Last updated: 12/17/2025, 1:30:37 PM
1class Solution {
2public:
3    long long maximumProfit(vector<int>& prices, int k) {
4        int n = prices.size();
5        vector memo(n, vector<array<long long, 3>>(k + 1, {-1, -1, -1}));
6        auto dfs = [&](this auto&& dfs, int i, int j, int end_state) -> long long {
7            if (j < 0) {
8                return LLONG_MIN / 2; 
9            }
10            if (i < 0) {
11                return end_state ? LLONG_MIN / 2 : 0;
12            }
13            long long& res = memo[i][j][end_state]; 
14            if (res != -1) { 
15                return res;
16            }
17            int p = prices[i];
18            if (end_state == 0) {
19                return res = max({dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p});
20            }
21            if (end_state == 1) {
22                return res = max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p);
23            }
24            return res = max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p);
25        };
26        return dfs(n - 1, k, 0);
27    }
28};