# Last updated: 8/24/2025, 10:44:16 AM
class Solution:
  def maxAdjacentDistance(self, nums: list[int]) -> int:
    return max(abs(nums[i] - nums[i - 1])
               for i in range(len(nums)))