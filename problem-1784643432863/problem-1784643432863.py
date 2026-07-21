# Last updated: 7/21/2026, 7:47:12 PM
1class Solution:
2  def maxActiveSectionsAfterTrade(self, s: str) -> int:
3    zeroGroups = [len(list(g)) for c, g in itertools.groupby(s) if c == '0']
4    return s.count('1') + max(map(sum, pairwise(zeroGroups)), default=0)