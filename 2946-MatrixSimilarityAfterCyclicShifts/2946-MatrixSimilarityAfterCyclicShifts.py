# Last updated: 3/27/2026, 7:59:31 PM
1class Solution:
2  def areSimilar(self, mat: list[list[int]], k: int) -> bool:
3    n = len(mat[0])
4    for row in mat:
5      for j in range(n):
6        if row[j] != row[(j + k) % n]:
7          return False
8    return True