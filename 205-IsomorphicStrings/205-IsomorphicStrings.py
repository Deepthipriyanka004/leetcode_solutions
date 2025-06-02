# Last updated: 6/2/2025, 6:38:30 PM
class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    return [*map(s.index, s)] == [*map(t.index, t)]