# Last updated: 1/21/2026, 10:57:02 AM
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4        for x in nums:
5            if x == 2:
6                ans.append(-1)
7            else:
8                for i in range(1, 32):
9                    if x >> i & 1 ^ 1:
10                        ans.append(x ^ 1 << (i - 1))
11                        break
12        return ans