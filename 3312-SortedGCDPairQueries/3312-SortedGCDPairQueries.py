# Last updated: 7/17/2026, 7:14:26 PM
1class Solution:
2  def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
3    maxNum = max(nums)
4    # countDivisor[d] := the number of `nums` having `num % d == 0`
5    countDivisor = [0] * (maxNum + 1)
6    # countGcdPair[g] := the number of pairs having gcd == g
7    countGcdPair = [0] * (maxNum + 1)
8
9    for num in nums:
10      for i in range(1, math.isqrt(num) + 1):
11        if num % i == 0:
12          countDivisor[i] += 1
13          if i != num // i:
14            countDivisor[num // i] += 1
15
16    for gcd in range(maxNum, 0, -1):
17      # There are C(countDivisor[gcd], 2) pairs that have a common divisor
18      # that's a multiple of `gcd` (including the one that equals to `gcd`).
19      # So, substract the multiples of `gcd` to have the number of pairs with a
20      # gcd that's exactly `gcd`.
21      countGcdPair[gcd] = countDivisor[gcd] * (countDivisor[gcd] - 1) // 2
22      for largerGcd in range(2 * gcd, maxNum + 1, gcd):
23        countGcdPair[gcd] -= countGcdPair[largerGcd]
24
25    # prefixCountGcdPair[g] := the number of pairs having gcd <= g
26    prefixCountGcdPair = list(itertools.accumulate(countGcdPair))
27    return [bisect.bisect_left(prefixCountGcdPair, query + 1)
28            for query in queries]