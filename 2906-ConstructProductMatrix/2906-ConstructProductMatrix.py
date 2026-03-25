# Last updated: 3/25/2026, 9:47:11 AM
1class Solution:
2  def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
3    MOD = 12345
4    m = len(grid)
5    n = len(grid[0])
6    ans = [[0] * n for _ in range(m)]
7    prefix = [1]
8    suffix = 1
9
10    for row in grid:
11      for num in row:
12        prefix.append(prefix[-1] * num % MOD)
13
14    for i in reversed(range(m)):
15      for j in reversed(range(n)):
16        ans[i][j] = prefix[i * n + j] * suffix % MOD
17        suffix = suffix * grid[i][j] % MOD
18
19    return ans