# Last updated: 1/17/2026, 6:20:58 PM
1class Solution:
2  def largestSquareArea(
3      self,
4      bottomLeft: list[list[int]],
5      topRight: list[list[int]],
6  ) -> int:
7    minSide = 0
8
9    for ((ax1, ay1), (ax2, ay2)), ((bx1, by1), (bx2, by2)) in (
10            itertools.combinations(zip(bottomLeft, topRight), 2)):
11      overlapX = min(ax2, bx2) - max(ax1, bx1)
12      overlapY = min(ay2, by2) - max(ay1, by1)
13      minSide = max(minSide, min(overlapX, overlapY))
14
15    return minSide**2