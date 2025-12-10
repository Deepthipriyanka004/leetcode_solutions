# Last updated: 12/10/2025, 7:13:06 PM
1class Solution:
2    def countPermutations(self, complexity: List[int]) -> int:
3        mod = 10**9 + 7
4        ans = 1
5        for i in range(1, len(complexity)):
6            if complexity[i] <= complexity[0]:
7                return 0
8            ans = ans * i % mod
9        return ans