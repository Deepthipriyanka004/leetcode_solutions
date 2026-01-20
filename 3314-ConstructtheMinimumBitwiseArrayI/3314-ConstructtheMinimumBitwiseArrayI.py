# Last updated: 1/20/2026, 10:56:27 AM
1class Solution:
2  def minBitwiseArray(self, nums: list[int]) -> list[int]:
3    return [-1 if num == 2 else num - self._getLeadingOneOfLastGroupOfOnes(num)
4            for num in nums]
5
6  def _getLeadingOneOfLastGroupOfOnes(self, num: int) -> int:
7    """
8    Returns the leading one of the last group of 1s in the binary
9    representation of num. For example, if num = 0b10111, the leading one of
10    the last group of 1s is 0b100.
11    """
12    leadingOne = 1
13    while (num & leadingOne) > 0:
14      leadingOne <<= 1
15    return leadingOne >> 1