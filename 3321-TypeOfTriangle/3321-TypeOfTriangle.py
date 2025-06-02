# Last updated: 6/2/2025, 6:30:45 PM
class Solution:
  def triangleType(self, nums: list[int]) -> str:
    nums.sort()
    if nums[0] + nums[1] <= nums[2]:
      return 'none'
    if nums[0] == nums[1] and nums[1] == nums[2]:
      return 'equilateral'
    if nums[0] == nums[1] or nums[1] == nums[2]:
      return 'isosceles'
    return 'scalene'