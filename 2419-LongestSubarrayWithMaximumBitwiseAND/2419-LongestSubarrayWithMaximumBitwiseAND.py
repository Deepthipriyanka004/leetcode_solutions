# Last updated: 7/30/2025, 9:26:39 AM
class Solution:
  def longestSubarray(self, nums: list[int]) -> int:
    ans = 0
    maxIndex = 0
    sameNumLength = 0

    for i, num in enumerate(nums):
      if nums[i] == nums[maxIndex]:
        sameNumLength += 1
        ans = max(ans, sameNumLength)
      elif nums[i] > nums[maxIndex]:
        maxIndex = i
        sameNumLength = 1
        ans = 1
      else:
        sameNumLength = 0

    return ans