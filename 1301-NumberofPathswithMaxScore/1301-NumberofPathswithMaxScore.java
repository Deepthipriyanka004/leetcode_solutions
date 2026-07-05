// Last updated: 7/5/2026, 10:12:25 AM
1class Solution {
2  public int[] pathsWithMaxScore(List<String> board) {
3    final int MOD = 1_000_000_007;
4    final int[][] DIRS = {{0, 1}, {1, 0}, {1, 1}};
5    final int n = board.size();
6    // dp[i][j] := the maximum sum from (n - 1, n - 1) to (i, j)
7    int[][] dp = new int[n + 1][n + 1];
8    Arrays.stream(dp).forEach(A -> Arrays.fill(A, -1));
9    // count[i][j] := the number of paths to get dp[i][j] from (n - 1, n - 1) to (i, j)
10    int[][] count = new int[n + 1][n + 1];
11
12    dp[0][0] = 0;
13    dp[n - 1][n - 1] = 0;
14    count[n - 1][n - 1] = 1;
15
16    for (int i = n - 1; i >= 0; --i)
17      for (int j = n - 1; j >= 0; --j) {
18        if (board.get(i).charAt(j) == 'S' || board.get(i).charAt(j) == 'X')
19          continue;
20        for (int[] dir : DIRS) {
21          final int x = i + dir[0];
22          final int y = j + dir[1];
23          if (dp[i][j] < dp[x][y]) {
24            dp[i][j] = dp[x][y];
25            count[i][j] = count[x][y];
26          } else if (dp[i][j] == dp[x][y]) {
27            count[i][j] += count[x][y];
28            count[i][j] %= MOD;
29          }
30        }
31        // If there's path(s) from 'S' to (i, j) and the cell is not 'E'.
32        if (dp[i][j] != -1 && board.get(i).charAt(j) != 'E') {
33          dp[i][j] += board.get(i).charAt(j) - '0';
34          dp[i][j] %= MOD;
35        }
36      }
37
38    return new int[] {dp[0][0], count[0][0]};
39  }
40}