# Last updated: 5/10/2026, 9:24:25 AM
1class Solution:
2  def maximumJumps(self, nums: list[int], target: int) -> int:
3    n = len(nums)
4    # dp[i] := the maximum number of jumps to reach i from 0
5    dp = [-1] * n
6    dp[0] = 0
7
8    for j in range(1, n):
9      for i in range(j):
10        if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
11          dp[j] = max(dp[j], dp[i] + 1)
12
13    return dp[-1]