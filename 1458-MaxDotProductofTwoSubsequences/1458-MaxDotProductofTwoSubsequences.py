# Last updated: 1/8/2026, 10:17:14 AM
1class Solution:
2  def maxDotProduct(self, A: list[int], B: list[int]) -> int:
3    m = len(A)
4    n = len(B)
5    # dp[i][j] := the maximum dot product of the two subsequences nums[0..i)
6    # and nums2[0..j)
7    dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]
8
9    for i in range(m):
10      for j in range(n):
11        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j],
12                               max(0, dp[i][j]) + A[i] * B[j])
13
14    return dp[m][n]