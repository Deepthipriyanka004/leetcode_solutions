# Last updated: 7/26/2026, 10:17:02 AM
1class Solution:
2  def maximumProduct(self, nums: list[int]) -> int:
3    nums.sort()
4    return max(nums[-1] * nums[0] * nums[1],
5               nums[-1] * nums[-2] * nums[-3])