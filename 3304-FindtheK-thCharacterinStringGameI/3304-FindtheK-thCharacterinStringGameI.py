# Last updated: 7/3/2025, 6:22:25 PM
class Solution:
  def kthCharacter(self, k: int) -> str:
    return string.ascii_lowercase[(k - 1).bit_count()]