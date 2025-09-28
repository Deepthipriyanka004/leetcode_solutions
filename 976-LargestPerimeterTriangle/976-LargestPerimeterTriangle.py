# Last updated: 9/28/2025, 4:58:49 PM
class Solution:
  def largestPerimeter(self, nums: list[int]) -> int:
    nums = sorted(nums)

    for i in range(len(nums) - 1, 1, -1):
      if nums[i - 2] + nums[i - 1] > nums[i]:
        return nums[i - 2] + nums[i - 1] + nums[i]

    return 0