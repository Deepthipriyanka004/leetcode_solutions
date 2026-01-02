# Last updated: 1/2/2026, 9:24:50 AM
1class Solution:
2  def repeatedNTimes(self, nums: list[int]) -> int:
3    for i in range(len(nums) - 2):
4      if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
5        return nums[i]
6    return nums[-1]