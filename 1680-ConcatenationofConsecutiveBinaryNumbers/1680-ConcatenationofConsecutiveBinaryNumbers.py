# Last updated: 2/28/2026, 10:14:51 AM
1class Solution:
2  def concatenatedBinary(self, n: int) -> int:
3    MOD = 1_000_000_007
4    ans = 0
5
6    def numberOfBits(n: int) -> int:
7      return int(math.log2(n)) + 1
8
9    for i in range(1, n + 1):
10      ans = ((ans << numberOfBits(i)) + i) % MOD
11
12    return ans