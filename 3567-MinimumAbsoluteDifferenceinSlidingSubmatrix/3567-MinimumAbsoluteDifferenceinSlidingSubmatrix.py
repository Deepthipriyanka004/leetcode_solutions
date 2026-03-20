# Last updated: 3/20/2026, 8:02:12 PM
1class Solution:
2    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
3        m, n = len(grid), len(grid[0])
4        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
5        for i in range(m - k + 1):
6            for j in range(n - k + 1):
7                nums = []
8                for x in range(i, i + k):
9                    for y in range(j, j + k):
10                        nums.append(grid[x][y])
11                nums.sort()
12                d = min((abs(a - b) for a, b in pairwise(nums) if a != b), default=0)
13                ans[i][j] = d
14        return ans