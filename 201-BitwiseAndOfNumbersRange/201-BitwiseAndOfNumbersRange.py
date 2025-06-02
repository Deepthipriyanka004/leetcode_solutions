# Last updated: 6/2/2025, 6:38:34 PM
class Solution:
  def rangeBitwiseAnd(self, m: int, n: int) -> int:
    return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1 if m < n else m