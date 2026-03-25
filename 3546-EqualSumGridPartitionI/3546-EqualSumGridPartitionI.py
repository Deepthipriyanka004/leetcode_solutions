# Last updated: 3/25/2026, 9:48:38 AM
1class Solution:
2  def canPartitionGrid(self, grid: list[list[int]]) -> bool:
3    totalSum = sum(map(sum, grid))
4
5    def canPartition(grid: list[list[int]]) -> bool:
6      runningSum = 0
7      for row in grid:
8        runningSum += sum(row)
9        if runningSum * 2 == totalSum:
10          return True
11      return False
12
13    return canPartition(grid) or canPartition(zip(*grid))