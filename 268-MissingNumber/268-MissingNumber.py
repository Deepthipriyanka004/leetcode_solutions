# Last updated: 6/2/2025, 6:38:04 PM
class Solution:
  def missingNumber(self, nums: list[int]) -> int:
    ans = len(nums)

    for i, num in enumerate(nums):
      ans ^= i ^ num

    return ans