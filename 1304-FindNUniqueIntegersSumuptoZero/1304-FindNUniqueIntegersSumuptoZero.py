# Last updated: 9/7/2025, 10:57:11 AM
class Solution:
  def sumZero(self, n: int) -> list[int]:
    return list(range(1 - n, n, 2))