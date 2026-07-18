# Last updated: 7/18/2026, 12:18:50 PM
1class Solution:
2  def findGCD(self, nums: list[int]) -> int:
3    return math.gcd(min(nums), max(nums))