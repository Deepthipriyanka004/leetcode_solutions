# Last updated: 4/2/2026, 9:16:41 PM
1class Solution:
2  def maximumAmount(self, coins: list[list[int]]) -> int:
3    m = len(coins)
4    n = len(coins[0])
5    # dp[i][j][k] := the maximum profit at position (i, j) with k remaining
6    # neutralizations
7    dp = [[[-math.inf] * 4 for _ in range(n)] for _ in range(m)]
8
9    # Base case: the robot starts at the top-left corner.
10    dp[0][0][2] = coins[0][0]
11    if coins[0][0] < 0:
12      dp[0][0][1] = 0  # Neutralize the robber.
13
14    for i in range(m):
15      for j in range(n):
16        for k in range(3):  # for each number of remaining neutralizations
17          if i > 0:
18            dp[i][j][k] = max(dp[i][j][k],
19                              dp[i - 1][j][k] + coins[i][j],
20                              dp[i - 1][j][k + 1])
21          if j > 0:
22            dp[i][j][k] = max(dp[i][j][k],
23                              dp[i][j - 1][k] + coins[i][j],
24                              dp[i][j - 1][k + 1])
25
26    return max(dp[-1][-1])