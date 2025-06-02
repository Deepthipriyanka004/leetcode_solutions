# Last updated: 6/2/2025, 6:36:46 PM
class Solution:
  def numTilings(self, n: int) -> int:
    MOD = 1_000_000_007
    dp = [0, 1, 2, 5] + [0] * 997

    for i in range(4, n + 1):
      dp[i] = 2 * dp[i - 1] + dp[i - 3]

    return dp[n] % MOD


