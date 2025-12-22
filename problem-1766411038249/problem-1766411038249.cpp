// Last updated: 12/22/2025, 7:13:58 PM
1class Solution {
2 public:
3  int minDeletionSize(vector<string>& strs) {
4    const int k = strs[0].length();
5    // dp[i] the length of LIS ending in strs[*][i]
6    vector<int> dp(k, 1);
7
8    for (int i = 1; i < k; ++i)
9      for (int j = 0; j < i; ++j)
10        if (ranges::all_of(strs, [&](const string& s) { return s[j] <= s[i]; }))
11          dp[i] = max(dp[i], dp[j] + 1);
12
13    return k - ranges::max(dp);
14  }
15};