# Last updated: 8/19/2025, 7:49:00 AM
class Solution:
  def zeroFilledSubarray(self, nums: list[int]) -> int:
    ans = 0
    indexBeforeZero = -1

    for i, num in enumerate(nums):
      if num:
        indexBeforeZero = i
      else:
        ans += i - indexBeforeZero

    return ans