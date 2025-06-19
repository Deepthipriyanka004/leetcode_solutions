# Last updated: 6/19/2025, 8:28:39 AM
class Solution:
  def partitionArray(self, nums: list[int], k: int) -> int:
    nums.sort()

    ans = 1
    mn = nums[0]

    for i in range(1, len(nums)):
      if mn + k < nums[i]:
        ans += 1
        mn = nums[i]

    return ans