# Last updated: 1/19/2026, 11:25:34 AM
1class Solution:
2  def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
3    m = len(mat)
4    n = len(mat[0])
5    ans = 0
6    prefix = [[0] * (n + 1) for _ in range(m + 1)]
7
8    for i in range(m):
9      for j in range(n):
10        prefix[i + 1][j + 1] = (mat[i][j] + prefix[i][j + 1] +
11                                prefix[i + 1][j] - prefix[i][j])
12
13    def squareSum(r1: int, c1: int, r2: int, c2: int) -> int:
14      return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]
15
16    for i in range(m):
17      for j in range(n):
18        for length in range(ans, min(m - i, n - j)):
19          if squareSum(i, j, i + length, j + length) > threshold:
20            break
21          ans = max(ans, length + 1)
22
23    return ans