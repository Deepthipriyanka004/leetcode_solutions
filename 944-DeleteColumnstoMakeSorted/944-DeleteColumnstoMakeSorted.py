# Last updated: 12/20/2025, 9:58:57 PM
1class Solution:
2  def minDeletionSize(self, strs: list[str]) -> int:
3    ans = 0
4
5    for j in range(len(strs[0])):
6      for i in range(len(strs) - 1):
7        if strs[i][j] > strs[i + 1][j]:
8          ans += 1
9          break
10
11    return ans