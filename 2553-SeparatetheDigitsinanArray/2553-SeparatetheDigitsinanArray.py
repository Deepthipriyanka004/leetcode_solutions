# Last updated: 5/11/2026, 9:03:57 PM
1class Solution:
2  def separateDigits(self, nums: list[int]) -> list[int]:
3    return [int(c) for num in nums for c in str(num)]