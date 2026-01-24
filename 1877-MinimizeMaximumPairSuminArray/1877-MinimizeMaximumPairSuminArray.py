# Last updated: 1/24/2026, 9:09:12 PM
1class Solution:
2  def minPairSum(self, nums: list[int]) -> int:
3    nums.sort()
4    return max(nums[i] + nums[len(nums) - 1 - i] for i in range(len(nums) // 2))