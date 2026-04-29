// Last updated: 4/29/2026, 7:19:41 PM
1class Solution {
2  public long maximumScore(int[][] grid) {
3    final int n = grid.length;
4    // prefix[j][i] := the sum of the first i elements in the j-th column
5    long[][] prefix = new long[n][n + 1];
6    // prevPick[i] := the maximum achievable score up to the previous column,
7    // where the bottommost selected element in that column is in row (i - 1)
8    long[] prevPick = new long[n + 1];
9    // prevSkip[i] := the maximum achievable score up to the previous column,
10    // where the bottommost selected element in the column before the previous
11    // one is in row (i - 1)
12    long[] prevSkip = new long[n + 1];
13
14    for (int j = 0; j < n; ++j)
15      for (int i = 0; i < n; ++i)
16        prefix[j][i + 1] = prefix[j][i] + grid[i][j];
17
18    for (int j = 1; j < n; ++j) {
19      long[] currPick = new long[n + 1];
20      long[] currSkip = new long[n + 1];
21      // Consider all possible combinations of the number of current and
22      // previous selected elements.
23      for (int curr = 0; curr <= n; ++curr)
24        for (int prev = 0; prev <= n; ++prev)
25          if (curr > prev) {
26            // 1. The current bottom is deeper than the previous bottom.
27            // Get the score of grid[prev..curr)[j - 1] for pick and skip.
28            final long score = prefix[j - 1][curr] - prefix[j - 1][prev];
29            currPick[curr] = Math.max(currPick[curr], prevSkip[prev] + score);
30            currSkip[curr] = Math.max(currSkip[curr], prevSkip[prev] + score);
31          } else {
32            // 2. The previous bottom is deeper than the current bottom.
33            // Get the score of grid[curr..prev)[j] for pick only.
34            final long score = prefix[j][prev] - prefix[j][curr];
35            currPick[curr] = Math.max(currPick[curr], prevPick[prev] + score);
36            currSkip[curr] = Math.max(currSkip[curr], prevPick[prev]);
37          }
38      prevPick = currPick;
39      prevSkip = currSkip;
40    }
41
42    return Arrays.stream(prevPick).max().getAsLong();
43  }
44}
45
46
47