# Last updated: 5/9/2026, 10:07:33 AM
1class Solution:
2  def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
3    m = len(grid)
4    n = len(grid[0])
5    t = 0  # the top
6    l = 0  # the left
7    b = m - 1  # the bottom
8    r = n - 1  # the right
9
10    while t < b and l < r:
11      elementInThisLayer = 2 * (b - t + 1) + 2 * (r - l + 1) - 4
12      netRotations = k % elementInThisLayer
13      for _ in range(netRotations):
14        topLeft = grid[t][l]
15        for j in range(l, r):
16          grid[t][j] = grid[t][j + 1]
17        for i in range(t, b):
18          grid[i][r] = grid[i + 1][r]
19        for j in range(r, l, - 1):
20          grid[b][j] = grid[b][j - 1]
21        for i in range(b, t, -1):
22          grid[i][l] = grid[i - 1][l]
23        grid[t + 1][l] = topLeft
24      t += 1
25      l += 1
26      b -= 1
27      r -= 1
28
29    return grid
30
31
32