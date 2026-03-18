# Last updated: 3/18/2026, 9:42:37 PM
1class Solution:
2  def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
3    m = len(grid)
4    n = len(grid[0])
5    ans = 0
6    # prefix[i][j] := the sum of matrix[0..i)[0..j)
7    prefix = [[0] * (n + 1) for _ in range(m + 1)]
8
9    for i in range(m):
10      for j in range(n):
11        prefix[i + 1][j + 1] = (grid[i][j] + prefix[i][j + 1] +
12                                prefix[i + 1][j] - prefix[i][j])
13        if prefix[i + 1][j + 1] <= k:
14          ans += 1
15
16    return ans