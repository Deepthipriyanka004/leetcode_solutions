# Last updated: 3/3/2026, 7:35:19 PM
1class Solution:
2  def findKthBit(self, n: int, k: int) -> str:
3    if n == 1:
4      return '0'
5    midIndex = pow(2, n - 1)  # 1-indexed
6    if k == midIndex:
7      return '1'
8    if k < midIndex:
9      return self.findKthBit(n - 1, k)
10    return '1' if self.findKthBit(n - 1, midIndex * 2 - k) == '0' else '0'