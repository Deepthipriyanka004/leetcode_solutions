# Last updated: 7/16/2026, 7:44:53 PM
1class Solution:
2    def gcdSum(self, nums: list[int]) -> int:
3        n = len(nums)
4        prefix_gcd = [0] * n
5        mx = 0
6        for i, x in enumerate(nums):
7            mx = max(mx, x)
8            prefix_gcd[i] = gcd(x, mx)
9        prefix_gcd.sort()
10        return sum(gcd(prefix_gcd[i], prefix_gcd[-i - 1]) for i in range(n // 2))