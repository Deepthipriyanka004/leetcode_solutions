# Last updated: 8/2/2026, 12:52:10 PM
1class Solution:
2  def stoneGame(self, piles: list[int]) -> bool:
3    n = len(piles)
4    # dp[i][j] := the maximum stones you can get more than your opponent in piles[i..j]
5    dp = [[0] * n for _ in range(n)]
6
7    for i, pile in enumerate(piles):
8      dp[i][i] = pile
9
10    for d in range(1, n):
11      for i in range(n - d):
12        j = i + d
13        dp[i][j] = max(piles[i] - dp[i + 1][j],
14                       piles[j] - dp[i][j - 1])
15
16    return dp[0][n - 1] > 0