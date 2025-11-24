# Last updated: 11/24/2025, 11:32:40 AM
class Solution:
  def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
    ans = []
    curr = 0

    for num in nums:
      curr = (curr * 2 + num) % 5
      ans.append(curr % 5 == 0)

    return ans


