# Last updated: 6/2/2025, 6:33:17 PM
class Solution:
  def numberOfArrays(
      self,
      differences: list[int],
      lower: int,
      upper: int,
  ) -> int:
    prefix = list(itertools.accumulate(differences, initial=0))
    return max(0, (upper - lower) - (max(prefix) - min(prefix)) + 1)