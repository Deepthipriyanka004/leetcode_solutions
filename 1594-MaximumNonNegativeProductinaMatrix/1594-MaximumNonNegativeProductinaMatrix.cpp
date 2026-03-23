// Last updated: 3/23/2026, 7:07:31 PM
1class Solution {
2 public:
3  int maxProductPath(vector<vector<int>>& grid) {
4    constexpr int kMod = 1'000'000'007;
5    const int m = grid.size();
6    const int n = grid[0].size();
7    // dpMin[i][j] := the minimum product from (0, 0) to (i, j)
8    // dpMax[i][j] := the maximum product from (0, 0) to (i, j)
9    vector<vector<long>> dpMin(m, vector<long>(n));
10    vector<vector<long>> dpMax(m, vector<long>(n));
11
12    dpMin[0][0] = dpMax[0][0] = grid[0][0];
13
14    for (int i = 1; i < m; ++i)
15      dpMin[i][0] = dpMax[i][0] = dpMin[i - 1][0] * grid[i][0];
16
17    for (int j = 1; j < n; ++j)
18      dpMin[0][j] = dpMax[0][j] = dpMin[0][j - 1] * grid[0][j];
19
20    for (int i = 1; i < m; ++i)
21      for (int j = 1; j < n; ++j)
22        if (grid[i][j] < 0) {
23          dpMin[i][j] = max(dpMax[i - 1][j], dpMax[i][j - 1]) * grid[i][j];
24          dpMax[i][j] = min(dpMin[i - 1][j], dpMin[i][j - 1]) * grid[i][j];
25        } else {
26          dpMin[i][j] = min(dpMin[i - 1][j], dpMin[i][j - 1]) * grid[i][j];
27          dpMax[i][j] = max(dpMax[i - 1][j], dpMax[i][j - 1]) * grid[i][j];
28        }
29
30    const long mx = max(dpMin.back().back(), dpMax.back().back());
31    return mx < 0 ? -1 : mx % kMod;
32  }
33};