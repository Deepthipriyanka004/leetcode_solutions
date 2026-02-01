# Last updated: 2/1/2026, 9:59:40 AM
1class Solution:
2  def minimumCost(self, nums: list[int]) -> int:
3    MAX = 50
4    min1 = MAX
5    min2 = MAX
6
7    for i in range(1, len(nums)):
8      if nums[i] < min1:
9        min2 = min1
10        min1 = nums[i]
11      elif nums[i] < min2:
12        min2 = nums[i]
13
14    return nums[0] + min1 + min2