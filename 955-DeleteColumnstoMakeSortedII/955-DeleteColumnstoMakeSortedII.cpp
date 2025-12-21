// Last updated: 12/21/2025, 8:51:39 AM
1class Solution {
2 public:
3  int minDeletionSize(vector<string>& strs) {
4    const int n = strs.size();
5    int ans = 0;
6    // sorted[i] := true if strs[i] < strs[i + 1]
7    vector<bool> sorted(n - 1);
8
9    for (int j = 0; j < strs[0].length(); ++j) {
10      int i;
11      for (i = 0; i + 1 < n; ++i)
12        if (!sorted[i] && strs[i][j] > strs[i + 1][j]) {
13          ++ans;
14          break;
15        }
16      // Already compared each pair, so update the sorted array if needed.
17      if (i + 1 == n)
18        for (i = 0; i + 1 < n; ++i)
19          sorted[i] = sorted[i] || strs[i][j] < strs[i + 1][j];
20    }
21
22    return ans;
23  }
24};
25