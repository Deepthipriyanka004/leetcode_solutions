# Last updated: 1/4/2026, 9:56:55 AM
1class Solution:
2  def sumFourDivisors(self, nums: list[int]) -> int:
3    ans = 0
4
5    for num in nums:
6      divisor = 0
7      for i in range(2, math.isqrt(num) + 1):
8        if num % i == 0:
9          if divisor == 0:
10            divisor = i
11          else:
12            divisor = 0
13            break
14      if divisor > 0 and divisor * divisor < num:
15        ans += 1 + num + divisor + num // divisor
16
17    return ans
18
19
20