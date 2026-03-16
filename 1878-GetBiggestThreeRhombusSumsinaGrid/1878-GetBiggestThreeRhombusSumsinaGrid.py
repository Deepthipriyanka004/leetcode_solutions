# Last updated: 3/16/2026, 10:21:06 AM
1class Solution:
2    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
3        m, n = len(grid), len(grid[0])
4        s1 = [[0] * (n + 2) for _ in range(m + 1)]
5        s2 = [[0] * (n + 2) for _ in range(m + 1)]
6        for i, row in enumerate(grid, 1):
7            for j, x in enumerate(row, 1):
8                s1[i][j] = s1[i - 1][j - 1] + x
9                s2[i][j] = s2[i - 1][j + 1] + x
10        ss = SortedSet()
11        for i, row in enumerate(grid, 1):
12            for j, x in enumerate(row, 1):
13                l = min(i - 1, m - i, j - 1, n - j)
14                ss.add(x)
15                for k in range(1, l + 1):
16                    a = s1[i + k][j] - s1[i][j - k]
17                    b = s1[i][j + k] - s1[i - k][j]
18                    c = s2[i][j - k] - s2[i - k][j]
19                    d = s2[i + k][j] - s2[i][j + k]
20                    ss.add(
21                        a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]
22                    )
23                while len(ss) > 3:
24                    ss.remove(ss[0])
25        return list(ss)[::-1]