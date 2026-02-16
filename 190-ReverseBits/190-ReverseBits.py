# Last updated: 2/16/2026, 9:54:08 AM
1class Solution:
2  def reverseBits(self, n: int) -> int:
3    ans = 0
4
5    for i in range(32):
6      if n >> i & 1:
7        ans |= 1 << 31 - i
8
9    return ans