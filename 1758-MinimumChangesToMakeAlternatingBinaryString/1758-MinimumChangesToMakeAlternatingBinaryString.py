# Last updated: 3/5/2026, 6:08:46 PM
1class Solution:
2  def minOperations(self, s: str) -> int:
3    # the cost to make s "1010"
4    cost10 = sum(int(c) == i % 2 for i, c in enumerate(s))
5    # the cost to make s "0101"
6    cost01 = len(s) - cost10
7    return min(cost10, cost01)