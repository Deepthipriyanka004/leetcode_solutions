# Last updated: 3/26/2026, 8:49:43 AM
1class Solution:
2  def canPartitionGrid(self, grid: list[list[int]]) -> bool:
3    summ = sum(map(sum, grid))
4
5    def canPartition(grid: list[list[int]]) -> bool:
6      topSum = 0
7      seen = set()
8      for i, row in enumerate(grid):
9        topSum += sum(row)
10        botSum = summ - topSum
11        seen |= set(row)
12        if topSum - botSum in (0, grid[0][0],  grid[0][-1], row[0]):
13          return True
14        if len(grid[0]) > 1 and i > 0 and topSum - botSum in seen:
15          return True
16      return False
17
18    return (canPartition(grid) or
19            canPartition(grid[::-1]) or
20            canPartition(list(zip(*grid))[::-1]) or
21            canPartition(list(zip(*grid))))