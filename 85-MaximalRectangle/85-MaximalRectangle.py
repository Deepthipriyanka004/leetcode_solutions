# Last updated: 1/11/2026, 10:40:14 AM
1class Solution:
2  def maximalRectangle(self, matrix: list[list[str]]) -> int:
3    if not matrix:
4      return 0
5
6    ans = 0
7    hist = [0] * len(matrix[0])
8
9    def largestRectangleArea(heights: list[int]) -> int:
10      ans = 0
11      stack = []
12
13      for i in range(len(heights) + 1):
14        while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
15          h = heights[stack.pop()]
16          w = i - stack[-1] - 1 if stack else i
17          ans = max(ans, h * w)
18        stack.append(i)
19
20      return ans
21
22    for row in matrix:
23      for i, num in enumerate(row):
24        hist[i] = 0 if num == '0' else hist[i] + 1
25      ans = max(ans, largestRectangleArea(hist))
26
27    return ans
28
29
30