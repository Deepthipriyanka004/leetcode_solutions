# Last updated: 2/18/2026, 9:52:52 AM
1class Solution:
2  def hasAlternatingBits(self, n: int) -> bool:
3    #            n = 0b010101
4    #       n >> 2 = 0b000101
5    # n ^ (n >> 2) = 0b010000 = a
6    #        a - 1 = 0b001111
7    #  a & (a - 1) = 0
8    a = n ^ (n >> 2)
9    return (a & (a - 1)) == 0