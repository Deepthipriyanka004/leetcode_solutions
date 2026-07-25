# Last updated: 7/25/2026, 10:22:21 AM
1class Solution:
2  def maxProduct(self, n: int) -> int:
3    s = sorted(str(n))
4    return int(s[-1]) * int(s[-2])