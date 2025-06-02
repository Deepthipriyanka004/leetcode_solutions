# Last updated: 6/2/2025, 6:37:58 PM
class Solution:
  def hIndex(self, citations: list[int]) -> int:
    n = len(citations)
    return n - bisect.bisect_left(range(n), n,
                                  key=lambda m: citations[m] + m)