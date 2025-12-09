# Last updated: 12/9/2025, 7:58:24 PM
1class Solution:
2  def countTriples(self, n: int) -> int:
3    ans = 0
4    squared = set()
5
6    for i in range(1, n + 1):
7      squared.add(i * i)
8
9    for a in squared:
10      for b in squared:
11        if a + b in squared:
12          ans += 1
13
14    return ans