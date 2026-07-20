# Last updated: 7/20/2026, 11:09:05 PM
1class Solution:
2  def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
3    m = len(grid)
4    n = len(grid[0])
5    ans = [[0] * n for _ in range(m)]
6
7    k %= m * n
8
9    for i in range(m):
10      for j in range(n):
11        index = (i * n + j + k) % (m * n)
12        x = index // n
13        y = index % n
14        ans[x][y] = grid[i][j]
15
16    return ans