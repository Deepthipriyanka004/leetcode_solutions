# Last updated: 7/14/2026, 9:27:38 PM
1class Solution:
2  def subsequencePairCount(self, nums: list[int]) -> int:
3    MOD = 1_000_000_007
4
5    @functools.lru_cache(None)
6    def dp(i: int, x: int, y: int) -> int:
7      if i == len(nums):
8        return int(x > 0 and x == y)
9      # 1. Skip nums[i]
10      skip = dp(i + 1, x, y)
11      # 2. Pick nums[i] in the first subsequence
12      take1 = dp(i + 1, math.gcd(x, nums[i]), y)
13      # 3. Pick nums[i] in the second subsequence
14      take2 = dp(i + 1, x, math.gcd(y, nums[i]))
15      return (skip + take1 + take2) % MOD
16
17    return dp(0, 0, 0)