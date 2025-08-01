# Last updated: 6/2/2025, 6:30:10 PM
class Solution:
  def minOperations(self, nums: list[int], k: int) -> int:
    numsSet = set(nums)
    mn = min(nums)
    if mn < k:
      return -1
    if mn > k:
      return len(numsSet)
    return len(numsSet) - 1