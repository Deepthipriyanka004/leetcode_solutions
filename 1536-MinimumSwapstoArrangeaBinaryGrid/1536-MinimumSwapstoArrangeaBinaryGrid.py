# Last updated: 3/2/2026, 9:32:53 AM
1class Solution:
2  def minSwaps(self, grid: list[list[int]]) -> int:
3    n = len(grid)
4    ans = 0
5    # suffixZeros[i] := the number of suffix zeros in the i-th row
6    suffixZeros = [n if 1 not in row else row[::-1].index(1) for row in grid]
7
8    for i in range(n):
9      neededZeros = n - 1 - i
10      # Get the first row with suffix zeros >= `neededZeros` in suffixZeros[i:..n).
11      j = next((j for j in range(i, n) if suffixZeros[j] >= neededZeros), -1)
12      if j == -1:
13        return -1
14      # Move the rows[j] to the rows[i].
15      for k in range(j, i, -1):
16        suffixZeros[k] = suffixZeros[k - 1]
17      ans += j - i
18
19    return ans