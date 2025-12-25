# Last updated: 12/25/2025, 8:34:27 AM
1class Solution:
2  def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
3    ans = 0
4    decremented = 0
5
6    happiness.sort(reverse=True)
7
8    for i in range(k):
9      ans += max(0, happiness[i] - decremented)
10      decremented += 1
11
12    return ans