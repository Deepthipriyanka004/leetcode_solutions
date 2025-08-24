# Last updated: 8/24/2025, 10:44:34 AM
class Solution:
  def possibleStringCount(self, word: str) -> int:
    return 1 + sum(a == b
                   for a, b in itertools.pairwise(word))