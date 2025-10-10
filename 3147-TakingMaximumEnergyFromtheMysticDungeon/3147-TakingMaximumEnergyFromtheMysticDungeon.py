# Last updated: 10/10/2025, 12:02:06 PM
class Solution:
  def maximumEnergy(self, energy: list[int], k: int) -> int:
    # dp[i] := the sum of energy starting at i
    dp = energy.copy()
    for i in range(len(energy) - 1 - k, -1, -1):
      dp[i] += dp[i + k]
    return max(dp)


