# Last updated: 12/4/2025, 7:19:15 PM
1class Solution:
2  def countCollisions(self, directions: str) -> int:
3    l = 0
4    r = len(directions) - 1
5
6    while l < len(directions) and directions[l] == 'L':
7      l += 1
8
9    while r >= 0 and directions[r] == 'R':
10      r -= 1
11
12    return sum(c != 'S' for c in directions[l:r + 1])