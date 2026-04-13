# Last updated: 4/13/2026, 8:15:18 PM
1class Solution:
2  def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
3    ans = math.inf
4
5    for i, num in enumerate(nums):
6      if num == target:
7        ans = min(ans, abs(i - start))
8
9    return ans