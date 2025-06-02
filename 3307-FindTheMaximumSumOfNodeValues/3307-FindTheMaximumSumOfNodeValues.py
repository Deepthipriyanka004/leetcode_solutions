# Last updated: 6/2/2025, 6:30:49 PM
class Solution:
  def maximumValueSum(
      self,
      nums: list[int],
      k: int,
      edges: list[list[int]],
  ) -> int:
    maxSum = sum(max(num, num ^ k) for num in nums)
    changedCount = sum((num ^ k) > num for num in nums)
    if changedCount % 2 == 0:
      return maxSum
    minChangeDiff = min(abs(num - (num ^ k)) for num in nums)
    return maxSum - minChangeDiff