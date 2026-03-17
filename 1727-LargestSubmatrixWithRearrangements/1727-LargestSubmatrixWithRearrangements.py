# Last updated: 3/17/2026, 8:40:39 PM
1class Solution:
2  def largestSubmatrix(self, matrix: list[list[int]]) -> int:
3    ans = 0
4    hist = [0] * len(matrix[0])
5
6    for row in matrix:
7      # Accumulate the histogram if possible.
8      for i, num in enumerate(row):
9        hist[i] = 0 if num == 0 else hist[i] + 1
10
11      # Get the sorted histogram.
12      sortedHist = sorted(hist)
13
14      # Greedily calculate the answer.
15      for i, h in enumerate(sortedHist):
16        ans = max(ans, h * (len(row) - i))
17
18    return ans
19