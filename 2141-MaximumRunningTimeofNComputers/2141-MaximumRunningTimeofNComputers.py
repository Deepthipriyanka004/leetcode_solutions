# Last updated: 12/1/2025, 9:49:15 PM
1class Solution:
2  def maxRunTime(self, n: int, batteries: list[int]) -> int:
3    summ = sum(batteries)
4
5    batteries.sort()
6
7    # The maximum battery is greater than the average, so it can last forever.
8    # Reduce the problem from size n to size n - 1.
9    while batteries[-1] > summ // n:
10      summ -= batteries.pop()
11      n -= 1
12
13    # If the maximum battery <= average running time, it won't be waste, and so
14    # do smaller batteries.
15    return summ // n