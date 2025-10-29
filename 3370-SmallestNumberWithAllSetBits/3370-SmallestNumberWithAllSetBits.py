# Last updated: 10/29/2025, 12:42:30 PM
class Solution:
  def smallestNumber(self, n: int) -> int:
    return (1 << n.bit_length()) - 1