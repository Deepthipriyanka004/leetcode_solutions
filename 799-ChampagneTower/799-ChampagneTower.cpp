// Last updated: 2/14/2026, 11:21:27 AM
1class Solution {
2 public:
3  double champagneTower(int poured, int query_row, int query_glass) {
4    vector<vector<double>> dp(query_row + 1, vector<double>(query_row + 1));
5    dp[0][0] = poured;
6
7    for (int i = 0; i < query_row; ++i)
8      for (int j = 0; j <= i; ++j)
9        if (dp[i][j] > 1) {
10          dp[i + 1][j] += (dp[i][j] - 1) / 2.0;
11          dp[i + 1][j + 1] += (dp[i][j] - 1) / 2.0;
12        }
13
14    return min(1.0, dp[query_row][query_glass]);
15  }
16};