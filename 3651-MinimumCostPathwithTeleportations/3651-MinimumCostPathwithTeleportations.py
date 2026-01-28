# Last updated: 1/28/2026, 9:33:02 AM
1class Solution:
2    def minCost(self, grid: List[List[int]], k: int) -> int:
3        m, n = len(grid), len(grid[0])
4        f = [[[inf] * n for _ in range(m)] for _ in range(k + 1)]
5        f[0][0][0] = 0
6        for i in range(m):
7            for j in range(n):
8                if i:
9                    f[0][i][j] = min(f[0][i][j], f[0][i - 1][j] + grid[i][j])
10                if j:
11                    f[0][i][j] = min(f[0][i][j], f[0][i][j - 1] + grid[i][j])
12        g = defaultdict(list)
13        for i, row in enumerate(grid):
14            for j, x in enumerate(row):
15                g[x].append((i, j))
16        keys = sorted(g, reverse=True)
17        for t in range(1, k + 1):
18            mn = inf
19            for key in keys:
20                pos = g[key]
21                for i, j in pos:
22                    mn = min(mn, f[t - 1][i][j])
23                for i, j in pos:
24                    f[t][i][j] = mn
25            for i in range(m):
26                for j in range(n):
27                    if i:
28                        f[t][i][j] = min(f[t][i][j], f[t][i - 1][j] + grid[i][j])
29                    if j:
30                        f[t][i][j] = min(f[t][i][j], f[t][i][j - 1] + grid[i][j])
31        return min(f[t][m - 1][n - 1] for t in range(k + 1))