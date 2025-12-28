# Last updated: 12/28/2025, 8:07:29 AM
1class Solution:
2  def countNegatives(self, grid: list[list[int]]) -> int:
3    m = len(grid)
4    n = len(grid[0])
5    ans = 0
6    i = m - 1
7    j = 0
8
9    while i >= 0 and j < n:
10      if grid[i][j] < 0:
11        ans += n - j
12        i -= 1
13      else:
14        j += 1
15
16    return ans