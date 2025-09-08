# Last updated: 9/8/2025, 8:08:57 PM
class Solution:
  def getNoZeroIntegers(self, n: int) -> list[int]:
    for A in range(n):
      B = n - A
      if '0' not in str(A) and '0' not in str(B):
        return A, B