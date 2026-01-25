# Last updated: 1/25/2026, 3:14:40 PM
1class Solution:
2  def minimumDifference(self, nums: list[int], k: int) -> int:
3    nums.sort()
4    ans = nums[k - 1] - nums[0]
5
6    for i in range(k, len(nums)):
7      ans = min(ans, nums[i] - nums[i - k + 1])
8
9    return ans