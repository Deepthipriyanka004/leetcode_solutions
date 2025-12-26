# Last updated: 12/26/2025, 9:28:26 AM
1class Solution:
2  def bestClosingTime(self, customers: str) -> int:
3    # Instead of computing the minimum penalty, we can compute the maximum profit.
4    ans = 0
5    profit = 0
6    maxProfit = 0
7
8    for i, customer in enumerate(customers):
9      profit += 1 if customer == 'Y' else -1
10      if profit > maxProfit:
11        maxProfit = profit
12        ans = i + 1
13
14    return ans