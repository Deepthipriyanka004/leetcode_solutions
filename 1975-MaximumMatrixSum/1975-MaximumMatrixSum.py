# Last updated: 1/5/2026, 12:18:18 PM
1class Solution:
2  def maxMatrixSum(self, matrix: list[list[int]]) -> int:
3    absSum = 0
4    minAbs = math.inf
5    # 0 := even number of negatives
6    # 1 := odd number of negatives
7    oddNeg = 0
8
9    for row in matrix:
10      for num in row:
11        absSum += abs(num)
12        minAbs = min(minAbs, abs(num))
13        if num < 0:
14          oddNeg ^= 1
15
16    return absSum - oddNeg * minAbs * 2