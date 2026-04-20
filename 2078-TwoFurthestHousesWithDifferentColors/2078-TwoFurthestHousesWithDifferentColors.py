# Last updated: 4/20/2026, 2:51:45 PM
1class Solution:
2  def maxDistance(self, colors: list[int]) -> int:
3    # The maximum distance always includes either the first or the last house.
4    n = len(colors)
5    i = 0  # the leftmost index, where colors[i] != colors[-1]
6    j = n - 1  # the rightmost index, where colors[j] != colors[0]
7    while colors[i] == colors[-1]:
8      i += 1
9    while colors[j] == colors[0]:
10      j -= 1
11    return max(n - 1 - i, j)