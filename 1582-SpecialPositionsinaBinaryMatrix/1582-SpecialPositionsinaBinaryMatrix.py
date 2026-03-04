# Last updated: 3/4/2026, 1:20:33 PM
1class Solution:
2  def numSpecial(self, mat: list[list[int]]) -> int:
3    m = len(mat)
4    n = len(mat[0])
5    ans = 0
6    rowOnes = [0] * m
7    colOnes = [0] * n
8
9    for i in range(m):
10      for j in range(n):
11        if mat[i][j] == 1:
12          rowOnes[i] += 1
13          colOnes[j] += 1
14
15    for i in range(m):
16      for j in range(n):
17        if mat[i][j] == 1 and rowOnes[i] == 1 and colOnes[j] == 1:
18          ans += 1
19
20    return ans