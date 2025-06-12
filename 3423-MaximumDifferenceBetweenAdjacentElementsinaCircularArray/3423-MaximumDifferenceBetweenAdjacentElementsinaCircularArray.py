# Last updated: 6/12/2025, 1:47:35 PM
class Solution:
  def maxAdjacentDistance(self, nums: list[int]) -> int:
    return max(abs(nums[i] - nums[i - 1])
               for i in range(len(nums)))