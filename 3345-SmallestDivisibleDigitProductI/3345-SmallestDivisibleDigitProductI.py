# Last updated: 8/6/2026, 3:09:03 PM
1class Solution:
2  def smallestNumber(self, n: int, t: int) -> int:
3    return next(num for num in range(n, n + 10)
4                if self._getDigitProd(num) % t == 0)
5
6  def _getDigitProd(self, num: int) -> int:
7    digitProd = 1
8    while num > 0:
9      digitProd *= num % 10
10      num //= 10
11    return digitProd