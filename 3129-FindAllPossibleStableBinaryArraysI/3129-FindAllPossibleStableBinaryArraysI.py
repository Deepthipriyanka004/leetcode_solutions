# Last updated: 3/9/2026, 9:18:30 AM
1class Solution:
2  # Same as 3129. Find All Possible Stable Binary Arrays I
3  def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
4    MOD = 1_000_000_007
5    # dp[i][j][k] := the number of stable arrays, where the number of
6    # occurrences of 0 is i and the number of occurrences of 1 is j and the last
7    # number is k (0/1)
8    dp = [[[0] * 2
9           for _ in range(one + 1)]
10          for _ in range(zero + 1)]
11
12    for i in range(min(zero, limit) + 1):
13      dp[i][0][0] = 1
14
15    for j in range(min(one, limit) + 1):
16      dp[0][j][1] = 1
17
18    for i in range(1, zero + 1):
19      for j in range(1, one + 1):
20        dp[i][j][0] = (
21            dp[i - 1][j][0] + dp[i - 1][j][1] -
22            (dp[i - limit - 1][j][1] if i - limit >= 1 else 0) + MOD) % MOD
23        dp[i][j][1] = (
24            dp[i][j - 1][0] + dp[i][j - 1][1] -
25            (dp[i][j - limit - 1][0] if j - limit >= 1 else 0) + MOD) % MOD
26
27    return (dp[zero][one][0] + dp[zero][one][1]) % MOD