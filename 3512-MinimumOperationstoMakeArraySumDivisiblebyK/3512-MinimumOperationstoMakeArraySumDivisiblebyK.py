# Last updated: 11/29/2025, 7:46:09 PM
1class Solution:
2  def minOperations(self, nums: list[int], k: int) -> int:
3    return sum(nums) % k