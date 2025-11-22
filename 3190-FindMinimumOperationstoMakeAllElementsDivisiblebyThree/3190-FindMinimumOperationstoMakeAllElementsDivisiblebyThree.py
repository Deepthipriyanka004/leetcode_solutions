# Last updated: 11/22/2025, 9:43:48 AM
class Solution:
  def minimumOperations(self, nums: list[int]) -> int:
    return sum(num % 3 != 0 for num in nums)