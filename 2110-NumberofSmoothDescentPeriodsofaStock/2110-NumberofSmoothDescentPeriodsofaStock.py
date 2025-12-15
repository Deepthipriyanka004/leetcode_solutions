# Last updated: 12/15/2025, 8:17:45 PM
1class Solution:
2  def getDescentPeriods(self, prices: list[int]) -> int:
3    ans = 1  # prices[0]
4    dp = 1
5
6    for i in range(1, len(prices)):
7      if prices[i] == prices[i - 1] - 1:
8        dp += 1
9      else:
10        dp = 1
11      ans += dp
12
13    return ans