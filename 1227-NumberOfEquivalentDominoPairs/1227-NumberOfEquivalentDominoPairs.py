# Last updated: 6/2/2025, 6:35:49 PM
class Solution:
  def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
    ans = 0
    count = collections.Counter()

    for domino in dominoes:
      key = min(domino[0], domino[1]) * 10 + max(domino[0], domino[1])
      ans += count[key]
      count[key] += 1

    return ans