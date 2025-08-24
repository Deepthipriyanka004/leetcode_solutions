# Last updated: 8/24/2025, 10:44:37 AM
class Solution:
  def kthCharacter(self, k: int) -> str:
    return string.ascii_lowercase[(k - 1).bit_count()]