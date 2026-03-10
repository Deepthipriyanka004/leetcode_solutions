// Last updated: 3/10/2026, 9:10:51 PM
1class Solution {
2 public:
3  // Same as 3129. Find All Possible Stable Binary Arrays I
4  int numberOfStableArrays(int zero, int one, int limit) {
5    constexpr int kMod = 1'000'000'007;
6    // dp[i][j][k] := the number of stable arrays, where the number of
7    // ocurrences of 0 is i and the number of ocurrences of 1 is j and the last
8    // number is k (0/1)
9    vector<vector<vector<long>>> dp(
10        zero + 1, vector<vector<long>>(one + 1, vector<long>(2)));
11
12    for (int i = 0; i <= min(zero, limit); ++i)
13      dp[i][0][0] = 1;
14
15    for (int j = 0; j <= min(one, limit); ++j)
16      dp[0][j][1] = 1;
17
18    for (int i = 1; i <= zero; ++i)
19      for (int j = 1; j <= one; ++j) {
20        dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1] -
21                       (i - limit < 1 ? 0 : dp[i - limit - 1][j][1]) + kMod) %
22                      kMod;
23        dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1] -
24                       (j - limit < 1 ? 0 : dp[i][j - limit - 1][0]) + kMod) %
25                      kMod;
26      }
27
28    return (dp[zero][one][0] + dp[zero][one][1]) % kMod;
29  }
30};