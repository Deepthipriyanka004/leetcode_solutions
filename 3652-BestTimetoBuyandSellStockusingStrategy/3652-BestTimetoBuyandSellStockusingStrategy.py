# Last updated: 12/18/2025, 8:39:57 PM
1class Solution:
2    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
3        n = len(prices)
4        s = [0] * (n + 1)
5        t = [0] * (n + 1)
6        for i, (a, b) in enumerate(zip(prices, strategy), 1):
7            s[i] = s[i - 1] + a * b
8            t[i] = t[i - 1] + a
9        ans = s[n]
10        for i in range(k, n + 1):
11            ans = max(ans, s[n] - (s[i] - s[i - k]) + t[i] - t[i - k // 2])
12        return ans