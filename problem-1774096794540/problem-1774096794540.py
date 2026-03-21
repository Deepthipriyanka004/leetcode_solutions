# Last updated: 3/21/2026, 6:09:54 PM
1class Solution:
2    def reverseSubmatrix(
3        self, grid: List[List[int]], x: int, y: int, k: int
4    ) -> List[List[int]]:
5        for i in range(x, x + k // 2):
6            i2 = x + k - 1 - (i - x)
7            for j in range(y, y + k):
8                grid[i][j], grid[i2][j] = grid[i2][j], grid[i][j]
9        return grid