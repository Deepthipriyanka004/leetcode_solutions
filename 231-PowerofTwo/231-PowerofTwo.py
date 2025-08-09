# Last updated: 8/9/2025, 10:26:21 PM
class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    return n >= 0 and n.bit_count() == 1