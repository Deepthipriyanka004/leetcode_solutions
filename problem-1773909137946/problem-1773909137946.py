# Last updated: 3/19/2026, 2:02:17 PM
1class Solution:
2  def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
3    m = len(grid)
4    n = len(grid[0])
5    ans = 0
6    # x[i][j] := the number of 'X' in grid[0..i)[0..j)
7    x = [[0] * (n + 1) for _ in range(m + 1)]
8    # y[i][j] := the number of 'Y' in grid[0..i)[0..j)
9    y = [[0] * (n + 1) for _ in range(m + 1)]
10
11    for i, row in enumerate(grid):
12      for j, cell in enumerate(row):
13        x[i + 1][j + 1] = (cell == 'X') + x[i][j + 1] + x[i + 1][j] - x[i][j]
14        y[i + 1][j + 1] = (cell == 'Y') + y[i][j + 1] + y[i + 1][j] - y[i][j]
15        if x[i + 1][j + 1] > 0 and x[i + 1][j + 1] == y[i + 1][j + 1]:
16          ans += 1
17
18    return ans