# Last updated: 12/30/2025, 12:16:31 PM
1class Solution:
2  def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
3    def isMagic(i: int, j: int) -> int:
4      s = "".join(str(grid[i + num // 3][j + num % 3])
5                  for num in [0, 1, 2, 5, 8, 7, 6, 3])
6      return s in "43816729" * 2 or s in "43816729"[::-1] * 2
7
8    ans = 0
9
10    for i in range(len(grid) - 2):
11      for j in range(len(grid[0]) - 2):
12        if grid[i][j] % 2 == 0 and grid[i + 1][j + 1] == 5:
13          ans += isMagic(i, j)
14
15    return ans