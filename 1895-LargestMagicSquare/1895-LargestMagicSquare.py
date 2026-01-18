# Last updated: 1/18/2026, 10:02:58 AM
1class Solution:
2  def largestMagicSquare(self, grid: list[list[int]]) -> int:
3    m = len(grid)
4    n = len(grid[0])
5    # prefixRow[i][j] := the sum of the first j numbers in the i-th row
6    prefixRow = [[0] * (n + 1) for _ in range(m)]
7    # prefixCol[i][j] := the sum of the first j numbers in the i-th column
8    prefixCol = [[0] * (m + 1) for _ in range(n)]
9
10    for i in range(m):
11      for j in range(n):
12        prefixRow[i][j + 1] = prefixRow[i][j] + grid[i][j]
13        prefixCol[j][i + 1] = prefixCol[j][i] + grid[i][j]
14
15    def isMagicSquare(i: int, j: int, k: int) -> bool:
16      """Returns True if grid[i..i + k)[j..j + k) is a magic square."""
17      diag, antiDiag = 0, 0
18      for d in range(k):
19        diag += grid[i + d][j + d]
20        antiDiag += grid[i + d][j + k - 1 - d]
21      if diag != antiDiag:
22        return False
23      for d in range(k):
24        if self._getSum(prefixRow, i + d, j, j + k - 1) != diag:
25          return False
26        if self._getSum(prefixCol, j + d, i, i + k - 1) != diag:
27          return False
28      return True
29
30    def containsMagicSquare(k: int) -> bool:
31      """Returns True if the grid contains any magic square of size k x k."""
32      for i in range(m - k + 1):
33        for j in range(n - k + 1):
34          if isMagicSquare(i, j, k):
35            return True
36      return False
37
38    for k in range(min(m, n), 1, -1):
39      if containsMagicSquare(k):
40        return k
41
42    return 1
43
44  def _getSum(self, prefix: list[list[int]], i: int, l: int, r: int) -> int:
45    """Returns sum(grid[i][l..r]) or sum(grid[l..r][i])."""
46    return prefix[i][r + 1] - prefix[i][l]