# Last updated: 3/11/2026, 9:42:49 PM
1class Solution:
2  def bitwiseComplement(self, n: int) -> int:
3    mask = 1
4    while mask < n:
5      mask = (mask << 1) + 1
6    return mask ^ n