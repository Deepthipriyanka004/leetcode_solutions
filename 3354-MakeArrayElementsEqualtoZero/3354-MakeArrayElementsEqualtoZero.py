# Last updated: 10/28/2025, 8:32:22 PM
class Solution:
  def countValidSelections(self, nums: list[int]) -> int:
    ans = 0
    prefix = list(itertools.accumulate(nums))
    suffix = list(itertools.accumulate(nums[::-1]))[::-1]

    for i, num in enumerate(nums):
      if num > 0:
        continue
      if prefix[i] == suffix[i]:
        ans += 2  # Go to either direction.
      if abs(prefix[i] - suffix[i]) == 1:
        ans += 1  # Go to the direction with the larger sum.

    return ans