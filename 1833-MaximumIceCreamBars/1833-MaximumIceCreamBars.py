# Last updated: 6/21/2026, 2:14:39 PM
1class Solution:
2  def maxIceCream(self, costs: list[int], coins: int) -> int:
3    for i, cost in enumerate(sorted(costs)):
4      if coins >= cost:
5        coins -= cost
6      else:
7        return i
8
9    return len(costs)