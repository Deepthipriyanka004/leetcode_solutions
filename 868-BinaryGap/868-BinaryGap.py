# Last updated: 2/22/2026, 12:24:56 PM
1class Solution:
2  def binaryGap(self, n: int) -> int:
3    ans = 0
4    d = -32  # the distance between any two 1s
5
6    while n:
7      if n % 2 == 1:
8        ans = max(ans, d)
9        d = 0
10      n //= 2
11      d += 1
12
13    return ans