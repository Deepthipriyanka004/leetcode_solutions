# Last updated: 11/30/2025, 8:37:15 AM
1class Solution:
2  def minSubarray(self, nums: list[int], p: int) -> int:
3    summ = sum(nums)
4    remainder = summ % p
5    if remainder == 0:
6      return 0
7
8    ans = len(nums)
9    prefix = 0
10    prefixToIndex = {0: -1}
11
12    for i, num in enumerate(nums):
13      prefix += num
14      prefix %= p
15      target = (prefix - remainder + p) % p
16      if target in prefixToIndex:
17        ans = min(ans, i - prefixToIndex[target])
18      prefixToIndex[prefix] = i
19
20    return -1 if ans == len(nums) else ans
21