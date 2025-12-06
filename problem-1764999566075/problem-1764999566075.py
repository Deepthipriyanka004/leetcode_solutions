# Last updated: 12/6/2025, 11:09:26 AM
1class Solution:
2    def countPartitions(self, nums: List[int], k: int) -> int:
3        mod = 10**9 + 7
4        sl = SortedList()
5        n = len(nums)
6        f = [1] + [0] * n
7        g = [1] + [0] * n
8        l = 1
9        for r, x in enumerate(nums, 1):
10            sl.add(x)
11            while sl[-1] - sl[0] > k:
12                sl.remove(nums[l - 1])
13                l += 1
14            f[r] = (g[r - 1] - (g[l - 2] if l >= 2 else 0) + mod) % mod
15            g[r] = (g[r - 1] + f[r]) % mod
16        return f[n]