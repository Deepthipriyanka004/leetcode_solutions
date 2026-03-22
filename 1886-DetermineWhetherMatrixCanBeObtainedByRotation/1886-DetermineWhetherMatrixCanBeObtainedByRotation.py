# Last updated: 3/22/2026, 9:01:44 AM
1class Solution:
2  def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
3    for _ in range(4):
4      if mat == target:
5        return True
6      mat = [list(x) for x in zip(*mat[::-1])]
7    return False