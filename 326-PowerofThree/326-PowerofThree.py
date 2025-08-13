# Last updated: 8/13/2025, 7:40:26 AM
class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    return n > 0 and 3**19 % n == 0