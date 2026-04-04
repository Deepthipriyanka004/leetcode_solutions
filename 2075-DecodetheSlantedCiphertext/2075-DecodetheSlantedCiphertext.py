# Last updated: 4/4/2026, 10:13:22 PM
1class Solution:
2  def decodeCiphertext(self, encodedText: str, rows: int) -> str:
3    n = len(encodedText)
4    cols = n // rows
5
6    ans = []
7    matrix = [[' '] * cols for _ in range(rows)]
8
9    for i in range(rows):
10      for j in range(cols):
11        matrix[i][j] = encodedText[i * cols + j]
12
13    for col in range(cols):
14      i = 0
15      j = col
16      while i < rows and j < cols:
17        ans.append(matrix[i][j])
18        i += 1
19        j += 1
20
21    return ''.join(ans).rstrip()