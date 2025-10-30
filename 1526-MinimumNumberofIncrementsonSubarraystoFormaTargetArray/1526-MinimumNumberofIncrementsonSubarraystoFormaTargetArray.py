# Last updated: 10/30/2025, 11:03:33 AM
class Solution:
  def minNumberOperations(self, target: list[int]) -> int:
    ans = target[0]

    for a, b in zip(target, target[1:]):
      if a < b:
        ans += b - a

    return ans


