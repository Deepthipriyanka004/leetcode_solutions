# Last updated: 4/28/2026, 8:33:43 PM
1class Solution:
2  def minOperations(self, grid: list[list[int]], x: int) -> int:
3    arr = sorted([a for row in grid for a in row])
4    if any((a - arr[0]) % x for a in arr):
5      return -1
6
7    ans = 0
8
9    for a in arr:
10      ans += abs(a - arr[len(arr) // 2]) // x
11
12    return ans