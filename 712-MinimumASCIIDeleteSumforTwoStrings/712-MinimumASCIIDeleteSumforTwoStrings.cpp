// Last updated: 1/10/2026, 6:07:26 PM
1class Solution {
2 public:
3  int minimumDeleteSum(string s1, string s2) {
4    const int m = s1.length();
5    const int n = s2.length();
6    // dp[i][j] := the minimum cost to make s1[0..i) and s2[0..j) equal
7    vector<vector<int>> dp(m + 1, vector<int>(n + 1));
8
9    // Delete s1[i - 1].
10    for (int i = 1; i <= m; ++i)
11      dp[i][0] = dp[i - 1][0] + s1[i - 1];
12
13    // Delete s2[j - 1].
14    for (int j = 1; j <= n; ++j)
15      dp[0][j] = dp[0][j - 1] + s2[j - 1];
16
17    for (int i = 1; i <= m; ++i)
18      for (int j = 1; j <= n; ++j)
19        if (s1[i - 1] == s2[j - 1])
20          dp[i][j] = dp[i - 1][j - 1];
21        else
22          dp[i][j] = min(dp[i - 1][j] + s1[i - 1], dp[i][j - 1] + s2[j - 1]);
23
24    return dp[m][n];
25  }
26};